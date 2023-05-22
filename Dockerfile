FROM python:3.9-alpine

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

WORKDIR /app

# pip installs
COPY ./requirements.txt requirements.txt

RUN apk add --no-cache postgresql-libs \
 && apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev \
 && python3 -m pip install -r /app/requirements.txt --no-cache-dir \
 && apk --purge del .build-deps

COPY . /app

ENV PYTHONPATH "${PYTHONPATH}=/app"

# Start FastAPI
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]