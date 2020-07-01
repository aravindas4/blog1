FROM python:3.7 AS build
RUN mkdir -p /blog1/requirements
WORKDIR /blog1
COPY ./requirements/ /blog1/requirements
RUN pip install -r ./requirements/base.txt
COPY .  /blog1
CMD python manage.py runserver
