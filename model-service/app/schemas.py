from typing import Literal
from pydantic import BaseModel, Field

class HeartDiseaseData(BaseModel):
    age: int = Field(..., description="age of the patient [years]", ge=1, le=120)
    sex: Literal["M", "F"] = Field(..., description="sex of the patient")
    chest_pain_type: Literal["TA", "ATA", "NAP", "ASY"] = Field(..., description="chest pain type")
    resting_bp: int = Field(..., description="resting blood pressure [mm Hg]", ge=0)
    cholesterol: int = Field(..., description="serum cholesterol [mm/dl]", ge=0)
    fasting_bs: Literal[0, 1] = Field(..., description="fasting blood sugar > 120 mg/dl")
    resting_ecg: Literal["Normal", "ST", "LVH"] = Field(..., description="resting electrocardiogram results")
    max_hr: int = Field(..., description="maximum heart rate achieved", ge=60, le=202)
    exercise_angina: Literal["Y", "N"] = Field(..., description="exercise-induced angina")
    oldpeak: float = Field(..., description="oldpeak = ST", ge=0)
    st_slope: Literal["Up", "Flat", "Down"] = Field(..., description="slope of peak exercise ST segment")

class PredictionOutput(BaseModel):
    prediction: int
    probability: float
    model_version: str = "v1"