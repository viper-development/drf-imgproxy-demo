FROM python:3.8-buster

LABEL name=drf-imgproxy-demo \
      version=0.1.0 \
      maintainer="info@viper.dev"

CMD ["docker/run.sh"]

EXPOSE 8000

ENV APP_ROOT=/opt/app \
    APP_USER=app \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR $APP_ROOT

RUN useradd -d $APP_ROOT -r $APP_USER

RUN set -ex; \
    apt-get update; \
    apt-get install --no-install-recommends -y \
        sqlite3 \
        postgresql-client \
        ; \
    apt-get clean

RUN set -ex; \
    pip install --upgrade pip; \
    pip install --no-cache-dir \
        poetry \
        uvicorn \
        psycopg2-binary

COPY pyproject.toml $APP_ROOT
COPY poetry.lock $APP_ROOT

RUN poetry install --no-dev

COPY . $APP_ROOT

RUN SECRET_KEY=fake \
    DATABASE_URL=fake \
    IMGPROXY_PROTOCOL=fake \
    IMGPROXY_BUCKET_NAME=fake \
    IMGPROXY_KEY=fake \
    IMGPROXY_SALT=fake \
    IMGPROXY_HOST=fake \
    ./manage.py collectstatic --no-input
