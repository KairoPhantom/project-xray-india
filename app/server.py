#!/usr/bin/env python3
import os, json, sqlite3, uuid, hashlib
from contextlib import contextmanager
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from pathlib import Path
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
DB=ROOT/os.getenv('DB_PATH','data/project_xray.db')
PORT=int(os.getenv('PORT','8080'))
MAX=int(os.getenv('MAX_BODY_BYTES','2097152'))
TOKEN=os.getenv('ADMIN_TOKEN','change-before-deploy')
CLAIM_TYPES={'verified_fact','reported_allegation','official_claim','expert_assessment','data_inconsistency','audit_finding','court_finding'}
STATES={'candidate','reviewed','published','disputed','corrected','withdrawn'}

def now(): return datetime.now(timezone.utc).isoformat()
def uid(prefix): return prefix+'_'+uuid.uuid4().hex[:16]
def connect():
    DB.parent.mkdir(parents=True,exist_ok=True)
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; c.execute('PRAGMA foreign_keys=ON'); return c
@contextmanager
def db():
    c=connect()
    try:
        with c: yield c
    finally: c.close()
def init():
    with db() as c: c.executescript((ROOT/'db/schema.sql').read_text())
def audit(c,actor,action,typ,oid,detail=''):
    c.execute('INSERT INTO audit_events(actor,action,object_type,object_id,detail,created_at) VALUES(?,?,?,?,?,?)',(actor,action,typ,oid,detail,now()))
def rows(cur): return [dict(x) for x in cur.fetchall()]
def project_bundle(pid):
    with db() as c:
        p=c.execute('SELECT * FROM projects WHERE id=?',(pid,)).fetchone()
        if not p:return None
        return {'project':dict(p),'claims':rows(c.execute('SELECT * FROM claims WHERE project_id=? ORDER BY created_at',(pid,))), 'gaps':rows(c.execute('SELECT * FROM gaps WHERE project_id=? ORDER BY created_at',(pid,))), 'responses':rows(c.execute('SELECT * FROM responses WHERE project_id=? ORDER BY created_at',(pid,)))}

class H(BaseHTTPRequestHandler):
    server_version='ProjectXRay/0.1'
    def log_message(self,fmt,*args): print(json.dumps({'time':now(),'remote':self.client_address[0],'message':fmt%args}))
    def send_common_headers(self,code=200,ctype='application/json; charset=utf-8'):
        self.send_response(code); self.send_header('Content-Type',ctype); self.send_header('X-Content-Type-Options','nosniff'); self.send_header('X-Frame-Options','DENY'); self.send_header('Referrer-Policy','no-referrer'); self.send_header('Content-Security-Policy',"default-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline'; connect-src 'self'"); self.end_headers()
    def out(self,obj,code=200): self.send_common_headers(code); self.wfile.write(json.dumps(obj,ensure_ascii=False).encode())
    def text(self,s,code=200,ctype='text/plain; charset=utf-8'): self.send_common_headers(code,ctype); self.wfile.write(s.encode())
    def body(self):
        n=int(self.headers.get('Content-Length','0'))
        if n>MAX: raise ValueError('request too large')
        return json.loads(self.rfile.read(n) or b'{}')
    def admin(self): return self.headers.get('Authorization','')==f'Bearer {TOKEN}' and TOKEN!='change-before-deploy'
    def do_GET(self):
        path=urlparse(self.path).path
        if path in ('/health','/ready'): return self.out({'status':'ok','time':now()})
        if path=='/api/projects':
            with db() as c:return self.out({'projects':rows(c.execute('SELECT * FROM projects ORDER BY updated_at DESC'))})
        seg=[x for x in path.split('/') if x]
        if len(seg)>=3 and seg[:2]==['api','projects']:
            pid=seg[2]; b=project_bundle(pid)
            if not b:return self.out({'error':'not found'},404)
            if len(seg)==3:return self.out(b)
            if seg[3]=='report':
                p=b['project']; lines=[f"# Evidence report: {p['title']}",'',f"Generated: {now()}",f"Authority: {p['authority']}",'', '## Claims']
                for x in b['claims']: lines += [f"- [{x['claim_type']} / {x['publication_state']}] {x['text']}",f"  Source: {x['source_url']}"]
                lines += ['', '## Records not located']+[f"- {g['document_name']} — searched: {g['search_scope']} ({g['searched_at']})" for g in b['gaps']]
                return self.text('\n'.join(lines),ctype='text/markdown; charset=utf-8')
            if seg[3]=='rti':
                p=b['project']; items='\n'.join(f"{i+1}. Certified electronic copy of {g['document_name']}." for i,g in enumerate(b['gaps'])) or '1. No document gaps have been selected.'
                return self.text(f"Draft RTI request — not legal advice\n\nTo: Public Information Officer, {p['authority']}\nSubject: Records concerning {p['title']}\n\nPlease provide:\n{items}\n\nPlease provide records electronically where available.\nGenerated {now()}")
            if seg[3]=='audit':
                if not self.admin():return self.out({'error':'unauthorized'},401)
                with db() as c:return self.out({'events':rows(c.execute('SELECT * FROM audit_events WHERE object_id=? ORDER BY id',(pid,)))})
        if path=='/' or path=='/index.html': return self.serve('static/index.html','text/html; charset=utf-8')
        if path=='/app.js': return self.serve('static/app.js','application/javascript; charset=utf-8')
        if path=='/styles.css': return self.serve('static/styles.css','text/css; charset=utf-8')
        return self.out({'error':'not found'},404)
    def serve(self,rel,ctype):
        p=ROOT/rel
        if not p.exists():return self.out({'error':'not found'},404)
        self.send_common_headers(200,ctype); self.wfile.write(p.read_bytes())
    def do_POST(self):
        if not self.admin():return self.out({'error':'unauthorized; set ADMIN_TOKEN'},401)
        path=urlparse(self.path).path; seg=[x for x in path.split('/') if x]
        try:d=self.body()
        except Exception as e:return self.out({'error':str(e)},400)
        if path=='/api/projects':
            if not d.get('title'):return self.out({'error':'title required'},400)
            pid=uid('prj'); t=now()
            with db() as c:
                c.execute('INSERT INTO projects VALUES(?,?,?,?,?,?,?,?,?)',(pid,d['title'],d.get('authority',''),d.get('location',''),d.get('summary',''),d.get('status','research'),int(bool(d.get('synthetic',False))),t,t)); audit(c,'admin','create','project',pid)
            return self.out({'id':pid},201)
        if len(seg)==4 and seg[:2]==['api','projects']:
            pid,kind=seg[2],seg[3]
            if not project_bundle(pid):return self.out({'error':'project not found'},404)
            with db() as c:
                if kind=='claims':
                    ct=d.get('claim_type'); st=d.get('publication_state','candidate')
                    if ct not in CLAIM_TYPES or st not in STATES:return self.out({'error':'invalid claim type/state'},400)
                    if st in {'published','reviewed'} and (not d.get('source_url') or not d.get('reviewer') or not (d.get('passage') or d.get('page_ref'))):return self.out({'error':'reviewed/published claims require source, reviewer and passage/page'},400)
                    oid=uid('clm'); c.execute('INSERT INTO claims VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(oid,pid,ct,st,d.get('text',''),d.get('source_url',''),d.get('publisher',''),d.get('passage',''),d.get('page_ref',''),d.get('reviewer',''),now() if d.get('reviewer') else '',now()))
                elif kind=='gaps':
                    if not d.get('document_name') or not d.get('search_scope'):return self.out({'error':'document_name and search_scope required'},400)
                    oid=uid('gap'); c.execute('INSERT INTO gaps VALUES(?,?,?,?,?,?,?)',(oid,pid,d['document_name'],d['search_scope'],d.get('searched_at',now()),d.get('status','not_located'),now()))
                elif kind=='responses':
                    if not d.get('responder') or not d.get('text'):return self.out({'error':'responder and text required'},400)
                    oid=uid('rsp'); c.execute('INSERT INTO responses VALUES(?,?,?,?,?,?)',(oid,pid,d['responder'],d['text'],d.get('source_url',''),now()))
                else:return self.out({'error':'unknown collection'},404)
                audit(c,'admin','create',kind,oid,f'project={pid}')
            return self.out({'id':oid},201)
        return self.out({'error':'not found'},404)

if __name__=='__main__':
    init(); print(f'Project X-Ray listening on http://0.0.0.0:{PORT}'); ThreadingHTTPServer(('0.0.0.0',PORT),H).serve_forever()
