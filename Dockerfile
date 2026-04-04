<<<<<<< HEAD
FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn pydantic openai

CMD ["python", "-m", "uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "7860"]
=======
FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir pydantic fastapi uvicorn openai

CMD ["python", "inference.py"]
>>>>>>> 0c94d1aa3ad327c92e2fbd0af7b279095d94b96a
