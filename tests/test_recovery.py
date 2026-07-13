import sqlite3,tempfile,unittest
from pathlib import Path
from scripts.recovery import backup,restore,integrity
ROOT=Path(__file__).resolve().parents[1]
class TestRecovery(unittest.TestCase):
 def test_backup_and_clean_restore(self):
  with tempfile.TemporaryDirectory() as d:
   source=Path(d)/'source.db';c=sqlite3.connect(source);c.executescript((ROOT/'db/schema.sql').read_text());c.execute("INSERT INTO projects VALUES('prj_aaaaaaaaaaaaaaaa','Fixture','Authority','','','research',1,'t','t')");c.commit();c.close()
   archived=Path(d)/'backup.db';restored=Path(d)/'clean'/'restored.db';self.assertEqual(backup(source,archived)['integrity'],'ok');restore(archived,restored);self.assertEqual(integrity(restored)['integrity'],'ok')
   c=sqlite3.connect(restored);self.assertEqual(c.execute('SELECT title FROM projects').fetchone()[0],'Fixture');c.close()
 def test_refuses_overwrite_and_invalid_database(self):
  with tempfile.TemporaryDirectory() as d:
   bad=Path(d)/'bad.db';bad.write_text('not sqlite');dest=Path(d)/'dest.db'
   with self.assertRaises(Exception):restore(bad,dest)
if __name__=='__main__':unittest.main()
