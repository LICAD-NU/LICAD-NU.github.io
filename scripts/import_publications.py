#!/usr/bin/env python3
"""Import an exported bibliography into the Astro content collection.

Usage:
  python3 scripts/import_publications.py path/to/publications.csv
  python3 -m pip install bibtexparser
  python3 scripts/import_publications.py path/to/publications.bib
CSV columns: title, authors, year, venue, doi, url, type, area.
Keep a single deduplicated master export of ALL team members' publications.
"""
import argparse,csv,json,re,unicodedata
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]; OUT=HERE/'src/content/publications'
def slug(s):
 s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
 return re.sub('-+','-',re.sub('[^a-z0-9]+','-',s)).strip('-')[:83]
def clean(s):return str(s or '').strip().strip('{}')
def papers_csv(path):
 with path.open(encoding='utf-8-sig',newline='') as f:yield from csv.DictReader(f)
def papers_bib(path):
 try:import bibtexparser
 except ImportError:raise SystemExit('For BibTeX import, run: python3 -m pip install bibtexparser')
 data=bibtexparser.loads(path.read_text(encoding='utf-8'))
 for ent in data.entries:
  author=re.sub(r'\s+and\s+',', ',ent.get('author',''))
  yield dict(title=ent.get('title',''),authors=author,year=ent.get('year',''),venue=ent.get('journal') or ent.get('booktitle') or ent.get('publisher',''),doi=ent.get('doi',''),url=ent.get('url',''),type='Conference' if ent.get('ENTRYTYPE')=='inproceedings' else 'Journal',bibtex_key=ent.get('ID',''),bibtex_entry=ent)
def main():
 cli=argparse.ArgumentParser();cli.add_argument('source',type=Path);a=cli.parse_args();items=papers_bib(a.source) if a.source.suffix.lower()=='.bib' else papers_csv(a.source);new=skip=0
 for row in items:
  title=clean(row.get('title'));year=re.search(r'\d{4}',clean(row.get('year')))
  if not title or not year:skip+=1;continue
  yr=int(year.group());key=f'{yr}-{slug(title)}';path=OUT/(key+'.md')
  if path.exists():skip+=1;continue
  vals={'title':title,'authors':clean(row.get('authors') or row.get('author')),'year':yr,'venue':clean(row.get('venue') or row.get('journal')),'type':clean(row.get('type')) or 'Journal','category':'Collaborative'}
  if vals['type'] not in ('Journal','Conference','Preprint','Other'):vals['type']='Other'
  for f in ('doi','url','area'):
   if clean(row.get(f)):vals[f]=clean(row.get(f))
  if row.get('bibtex_entry'):
   ent=row['bibtex_entry'];entrytype=ent.get('ENTRYTYPE','article');ident=ent.get('ID',key)
   bits=['@'+entrytype+'{'+ident+',']+[f'  {f} = {{{v}}},' for f,v in ent.items() if f not in ('ENTRYTYPE','ID')]+['}']
   vals['bibtex']='\n'.join(bits)
  lines=['---']+[f'{k}: {json.dumps(v,ensure_ascii=False)}' for k,v in vals.items()]+['---','','Imported bibliography entry. Verify metadata and authorship before publication.','']
  path.write_text('\n'.join(lines),encoding='utf-8');new+=1
 print(f'Added {new} records; skipped {skip} duplicate/invalid records. Review records, then commit to GitHub.')
if __name__=='__main__':main()
