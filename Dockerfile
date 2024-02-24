FROM python:3.12.2-slim

WORKDIR /code

RUN pip install pipenv 

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system

COPY ./app /code/app