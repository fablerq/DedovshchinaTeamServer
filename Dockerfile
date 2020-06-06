FROM python:3.7.0-slim

ENV PYTHONUNBUFFERED=1

COPY . /app
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["sh", "./docker-entrypoint.sh"]