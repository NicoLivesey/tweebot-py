FROM python:3.7.2

LABEL maintainer="Nicolas HENRY nicolas.h@lajavanesss.com"

EXPOSE 80

WORKDIR /var/task

RUN apt-get update -y

COPY requirements/ .

RUN pip install --upgrade pip &&\
    pip install -r requirements_runtime.txt

COPY ./tweebot_py /tweebot_py

RUN bash /tweebot_py/setup/model.sh

CMD ["python", "/tweebot_py/app.py"]
