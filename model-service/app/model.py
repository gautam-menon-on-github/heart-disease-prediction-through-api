import logging
from pathlib import Path
from typing import Any
import numpy as np
import joblib

logger = logging.getLogger(__name__)

DEFAULT_MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "heart_disease_model.joblib"

class ModelWrapper:
    def __init__(self, model_path: Path = DEFAULT_MODEL_PATH) -> None:
        self.model_path = model_path
        self._model: Any = None

    def load_model(self) -> None:
        if self._model is not None:
            return

        if not self.model_path.exists():
            raise FileNotFoundError(f"Model artifact not found at {self.model_path}")

        try:
            self._model = joblib.load(self.model_path)
        except Exception as e:
            logger.exception("Failed to load model from %s", self.model_path)
            raise RuntimeError("Could not initialize machine learning model.") from e

    def predict(self, features: list[float] | np.ndarray) -> tuple[int, float]:
        self.load_model()
        feature_array = np.asarray(features, dtype=np.float64).reshape(1, -1)

        try:
            if hasattr(self._model, "predict_proba"):
                probabilities = self._model.predict_proba(feature_array)[0]
                probability = float(probabilities[1])
                prediction = int(probability >= 0.5)
            else:
                # Fallback for models without predict_proba: probability here
                # is a stand-in (1.0 / 0.0), not a calibrated confidence score.
                prediction = int(self._model.predict(feature_array)[0])
                probability = 1.0 if prediction == 1 else 0.0

            return prediction, probability

        except Exception as e:
            logger.exception("Inference failed for input: %s", feature_array.tolist())
            raise ValueError("Error running model inference.") from e

model_wrapper = ModelWrapper()