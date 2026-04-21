FROM python:3.14.4-slim
WORKDIR /app
COPY main.py .
CMD ["python", "main.py"]