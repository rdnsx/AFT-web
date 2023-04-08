FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py

VOLUME [ "/app/data" ]

CMD ["streamlit", "run", "app.py", "--server.port", "8080"]
