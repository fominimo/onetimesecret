FROM python:3.7

# set work directory
WORKDIR /code/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
# don't create .pyc files.
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt


# copy project
COPY . .