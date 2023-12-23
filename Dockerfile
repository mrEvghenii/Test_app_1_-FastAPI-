FROM python:3.10-alpine3.19

RUN mkdir "/Cafe_app"

WORKDIR /Cafe_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn main:app --workers 1 --workers-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8080

