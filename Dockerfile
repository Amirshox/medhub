FROM python:3.9-alpine

# envs
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TZ="Asia/Tashkent"

RUN pip3 install --upgrade pip

COPY requirements.txt .

RUN mkdir -p /app

RUN apk update \
    && apk add --no-cache --virtual build-deps \
    g++ \
    gcc \
    python3-dev \
    musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip3 install --no-cache-dir -r requirements.txt \
    && apk del --no-cache build-deps

WORKDIR /app
COPY . /app

COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]

