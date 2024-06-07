FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get -y install gcc

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./app.py .

CMD ["python", "app.py"]
