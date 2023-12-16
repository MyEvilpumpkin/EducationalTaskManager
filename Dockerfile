FROM python:3.11.7-slim

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY src/ /app

WORKDIR /app

ENTRYPOINT ["python3"]
