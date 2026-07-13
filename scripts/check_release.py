from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[1]
required=['README.md','AGENTS.md','LICENSE','SECURITY.md','CONTRIBUTING.md','CODE_OF_CONDUCT.md','docs/ROADMAP_72_HOURS.md','docs/ACCEPTANCE_CRITERIA.md','docs/EVIDENCE_POLICY.md','docs/THREAT_MODEL.md','Dockerfile','docker-compose.yml','app/server.py','tests/test_api.py']
missing=[x for x in required if not (root/x).exists()]
if missing: print('Missing:',*missing);sys.exit(1)
for p in root.rglob('*'):
 if p.is_file() and p.name not in {'.env.example','check_release.py'}:
  t=p.read_text(errors='ignore')
  secret_markers=['s'+'k-', 'BEGIN'+' PRIVATE KEY']
  if any(marker in t for marker in secret_markers): print('Potential secret:',p);sys.exit(1)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s',str(root/'tests'),'-v'],cwd=root)
sys.exit(r.returncode)
