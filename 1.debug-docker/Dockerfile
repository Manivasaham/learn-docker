FROM python:3.7.16-slim-bullseye

RUN mkdir /app
WORKDIR /app

COPY ./simple-loop.py .
ENTRYPOINT ["python3", "-u", "simple-loop.py"]
