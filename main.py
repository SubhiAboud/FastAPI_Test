# يتطلب: pip install fastapi uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Prediction Service")

class PredictionRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    label: str
    confidence: float

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    # هنا يتم استدعاء النموذج الحقيقي (sklearn / torch / LLM API)
    return PredictionResponse(label="positive", confidence=0.93)

# للتشغيل من الطرفية:
# uvicorn main:app --reload
# ثم افتح: http://127.0.0.1:8000/docs للتوثيق التفاعلي التلقائي

