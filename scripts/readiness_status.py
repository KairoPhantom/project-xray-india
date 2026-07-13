#!/usr/bin/env python3
from pathlib import Path
import sys
p=Path(__file__).resolve().parents[1]/'ops/production-readiness.yaml'
text=p.read_text()
items=[]
cur={}
for raw in text.splitlines():
    s=raw.strip()
    if s.startswith('- id:'):
        if cur: items.append(cur)
        cur={'id':s.split(':',1)[1].strip()}
    elif cur and s.startswith('status:'): cur['status']=s.split(':',1)[1].strip()
    elif cur and s.startswith('evidence:'): cur['evidence']=s.split(':',1)[1].strip()
if cur: items.append(cur)
passed=[x for x in items if x.get('status')=='passed' and x.get('evidence') not in (None,'null','')]
failed=[x for x in items if x not in passed]
print(f'Readiness: {len(passed)}/{len(items)} checks have passed with evidence')
for x in failed: print(f"PENDING {x['id']}")
sys.exit(0 if not failed else 1)
