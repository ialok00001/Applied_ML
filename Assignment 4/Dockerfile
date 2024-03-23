FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY score.py .
COPY model.pkl .

EXPOSE 5000

CMD ["python", "app.py"]
