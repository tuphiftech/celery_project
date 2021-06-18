FROM python:3
ENV PYTHONUNBUFFERED 1

USER root

WORKDIR code/

# RUN pip install --no-cache-dir -r requirements.txt

COPY requirements-lock.txt .

RUN pip install -U pip && \
    pip install -r requirements-lock.txt && \
    rm requirements-lock.txt

