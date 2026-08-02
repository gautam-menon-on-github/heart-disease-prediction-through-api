from pydantic import BaseModel, Field

class HeartDiseaseData(BaseModel):
    age: int = Field(..., description="age of the patient [years]", ge=1, le=120)
    sex: str = Field(..., description="sex of the patient [M: Male, F: Female] (Encoded: F -> 0; M -> 1)")
    chest_pain_type: str = Field(..., description="chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic] (Encoded: ASY -> 0; ATA -> 1; NAP -> 2; TA -> 3)")
    resting_bp: int = Field(..., description="resting blood pressure [mm Hg]", ge=0)
    cholesterol: int = Field(..., description="serum cholesterol [mm/dl]", ge=0)
    fasting_bs: int = Field(..., description="fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]")
    resting_ecg: str = Field(..., description="resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria] (Encoded: LVH -> 0; Normal -> 1; ST -> 2)")
    max_hr: int = Field(..., description="maximum heart rate achieved [Numeric value between 60 and 202]", ge=60, le=202)
    exercise_angina: str = Field(..., description="exercise-induced angina [Y: Yes, N: No] (Encoded: N -> 0; Y -> 1)")
    oldpeak: float = Field(..., description="oldpeak = ST [Numeric value measured in depression]", ge=0)
    st_slope: str = Field(..., description="the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping] (Encoded: Down -> 0; Flat -> 1; Up -> 2)")

class PredictionResponse(BaseModel):
    prediction: int = Field(..., description="Predicted class [0: Normal, 1: heart disease, ]")
    probability: float = Field(..., description="Probability of the prediction between 0 and 1")
    model_version: str = "v1"