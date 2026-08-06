FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt

COPY app/ ./app/
COPY models/ ./models/

RUN useradd --create-home appuser
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]