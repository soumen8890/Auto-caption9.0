FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Render will auto-detect PORT
CMD ["python", "main.py"]
