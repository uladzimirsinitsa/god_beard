# syntax=docker/dockerfile:1
FROM python:3.10.4-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY main.py main.py
COPY .env .env
CMD ["python", "main.py", "--host=0.0.0.0"]