cd ~/speedaf-project

# مجلدات
mkdir -p backend app tests

# FastAPI بسيط
cat > backend/main.py << 'PY'
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True}
PY

# تشغيل محليًا لاحقًا: uvicorn backend.main:app --reload

# متطلبات
cat > requirements.txt << 'REQ'
fastapi
uvicorn[standard]
google-cloud-aiplatform
google-cloud-bigquery
google-cloud-storage
pydantic
python-dotenv
REQ

# ملف README مبدئي محلي (لو ما كتبتوش من الواجهة)
cat > README.md << 'MD'
# speedaf-project

- Backend: FastAPI (`backend/main.py`)
- Local run: `uvicorn backend.main:app --reload`
- Dependencies: `pip install -r requirements.txt`
MD

# دفع التغييرات
git add .
git commit -m "Scaffold: FastAPI backend + requirements + README"
git push
