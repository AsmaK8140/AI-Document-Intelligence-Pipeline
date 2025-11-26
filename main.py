from src.project4.pipeline import run_document_pipeline
from pathlib import Path
p = Path('data/sample_docs/sample_doc_1.txt')
if not p.exists():
    print('No sample doc found. Create data/sample_docs/sample_doc_1.txt or upload via UI.')
else:
    out = run_document_pipeline(str(p), out_prefix='outputs/report_sample_doc_1')
    print('Output written to', out)
