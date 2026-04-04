FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir pydantic fastapi uvicorn openai

CMD ["python", "-m", "uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "7860"]