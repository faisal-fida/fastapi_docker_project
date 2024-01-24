FROM python:3.10.13-slim

WORKDIR /fastapi

COPY requirements.txt /fastapi/requirements.txt

RUN pip install --no-cache-dir -r /fastapi/requirements.txt

COPY app.py /fastapi/app.py

COPY scraper.py /fastapi/scraper.py
