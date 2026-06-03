FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m -u 1000 user

USER user

COPY app.py .

EXPOSE 5000

CMD ["python3","app.py"]
