#!/usr/bin/bash

#alembic upgrade head

#python insert_test_data.py

gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8080