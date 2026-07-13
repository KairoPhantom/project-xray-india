import os,tempfile,threading,json,urllib.request,unittest,sys
from pathlib import Path
TMP=tempfile.TemporaryDirectory(); os.environ['DB_PATH']=TMP.name+'/test.db'; os.environ['ADMIN_TOKEN']='test-secret'; os.environ['PORT']='18081'
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app import server
class TestCore(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  server.init(); cls.http=server.ThreadingHTTPServer(('127.0.0.1',18081),server.H); threading.Thread(target=cls.http.serve_forever,daemon=True).start()
 @classmethod
 def tearDownClass(cls): cls.http.shutdown(); TMP.cleanup()
 def req(self,path,method='GET',data=None,auth=False):
  h={'Content-Type':'application/json'}
  if auth:h['Authorization']='Bearer test-secret'
  q=urllib.request.Request('http://127.0.0.1:18081'+path,data=json.dumps(data).encode() if data is not None else None,headers=h,method=method)
  with urllib.request.urlopen(q) as r:return r.status, json.loads(r.read()) if 'json' in r.headers.get('Content-Type','') else r.read().decode()
 def test_end_to_end(self):
  s,p=self.req('/api/projects','POST',{'title':'Synthetic bridge','authority':'Example Authority','synthetic':True},True); self.assertEqual(s,201); pid=p['id']
  s,c=self.req(f'/api/projects/{pid}/claims','POST',{'claim_type':'official_claim','publication_state':'published','text':'Synthetic claim','source_url':'https://example.invalid/source','publisher':'Synthetic Publisher','passage':'Synthetic passage','reviewer':'reviewer-1'},True); self.assertEqual(s,201)
  self.req(f'/api/projects/{pid}/gaps','POST',{'document_name':'Synthetic test report','search_scope':'Synthetic fixture only'},True)
  self.req(f'/api/projects/{pid}/responses','POST',{'responder':'Example Authority','text':'Synthetic response'},True)
  s,b=self.req('/api/projects/'+pid); self.assertEqual(len(b['claims']),1); self.assertEqual(len(b['gaps']),1); self.assertEqual(len(b['responses']),1)
  s,r=self.req('/api/projects/'+pid+'/report'); self.assertIn('Synthetic claim',r)
  s,a=self.req('/api/projects/'+pid+'/audit',auth=True); self.assertGreaterEqual(len(a['events']),1)
 def test_health(self): self.assertEqual(self.req('/health')[0],200)
if __name__=='__main__':unittest.main()
