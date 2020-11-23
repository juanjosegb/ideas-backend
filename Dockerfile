FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements_dev.txt /code/
RUN pip install -r requirements_dev.txt
COPY . /code/