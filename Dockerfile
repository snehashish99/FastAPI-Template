FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app/

ENV PYTHONPATH=/app

COPY requirements.txt requirements.txt

RUN apt update
RUN pip install -r requirements.txt

COPY ./app /app
# Make entrypoint executable and run
RUN chmod 777 entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]