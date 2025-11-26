# AI Document Intelligence Pipeline — Enterprise PDF-to-Insights

This project ingests documents (PDF/DOCX/TXT), extracts and cleans text, chunks passages, and uses prompt-engineered LLM calls (stub mode) to produce executive summaries, section summaries, entities, Q&A, and action items.

## Quick start (stub mode)
1. Create venv: `python -m venv .venv`
2. Activate: Windows: `.venv\Scripts\activate`  Linux: `source .venv/bin/activate`
3. Install: `pip install -r requirements.txt`
4. Run sample: `python main.py` or `streamlit run app/streamlit_app.py`
5. Outputs are saved to `outputs/`

## Notes
- Project runs in **stub mode** by default (no OpenAI key required).
- Replace LLM stub with real OpenAI calls if needed (see src/project4/llm_client.py).
