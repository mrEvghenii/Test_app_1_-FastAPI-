FROM python:3.10

RUN mkdir "/Cafe_app"

WORKDIR /Cafe_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh

#CMD python3 insert_test_data.py
#
#CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8080

