from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from app.schemas import HeartDiseaseData, PredictionOutput
from app.model import model_wrapper

SEX_MAP = {"F": 0, "M": 1}
CP_MAP = {"ASY": 0, "ATA": 1, "NAP": 2, "TA": 3}
ECG_MAP = {"LVH": 0, "Normal": 1, "ST": 2}
ANGINA_MAP = {"N": 0, "Y": 1}
SLOPE_MAP = {"Down": 0, "Flat": 1, "Up": 2}

@asynccontextmanager
async def lifespan(app: FastAPI):
    model_wrapper.load_model()
    yield

app = FastAPI(title="Heart Disease Prediction Service", lifespan=lifespan)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionOutput)
def predict(payload: HeartDiseaseData):
    try:
        features = [
            payload.age,
            SEX_MAP[payload.sex],
            CP_MAP[payload.chest_pain_type],
            payload.resting_bp,
            payload.cholesterol,
            payload.fasting_bs,
            ECG_MAP[payload.resting_ecg],
            payload.max_hr,
            ANGINA_MAP[payload.exercise_angina],
            payload.oldpeak,
            SLOPE_MAP[payload.st_slope],
        ]
        prediction, probability = model_wrapper.predict(features)
        return PredictionOutput(prediction=prediction, probability=probability)
    except (FileNotFoundError, RuntimeError, ValueError) as e:
        raise HTTPException(status_code=500, detail=str(e))