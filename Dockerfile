FROM python:3.7.2

LABEL maintainer="Nicolas HENRY nicolas.h@lajavanesss.com"

EXPOSE 80

WORKDIR /var/task

RUN apt-get update -y

# ADD MODEL DOWNLOAD

COPY requirements/ .

RUN pip install --upgrade pip &&\
    pip install -r requirements/requirements_runtime.txt

COPY ./app /app

CMD ["python", "/app/app.py"]
