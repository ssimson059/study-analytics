# Study Assistant

## Domain
Education

## Files
- `index.html`
- `style.css`
- `script.js`
- `app.py`
- `requirements.txt`
- `README.md`
- `.gitignore`

## GitHub → Render deployment

1. Upload this folder to a GitHub repository.
2. In Render, create a **Web Service** and connect the repository.
3. Build Command:
   `pip install -r requirements.txt`
4. Start Command:
   `gunicorn app:app`
5. In Render → Environment, add:
   `GEMINI_API_KEY` = your Gemini API key
6. Deploy.

`.env` is intentionally NOT included. The API key stays in Render Environment Variables and is not placed in frontend JavaScript.

## Local run
```bash
pip install -r requirements.txt
python app.py
```

Open the URL shown by Flask.

## Security
Never commit your Gemini API key to GitHub.
