FROM python:3.9.10-alpine AS build
COPY requirements.txt .
RUN apk add -U --no-cache \
    gcc \
    build-base \
    linux-headers \
    ca-certificates \
    python3-dev \
    libffi-dev \
    libressl-dev \
    libxslt-dev \
    mariadb-connector-c \
    mariadb-dev
RUN pip install --user -r requirements.txt

FROM python:3.9.10-alpine
RUN adduser -u 82 -DSG www-data www-data; \
    apk add --no-cache \
        curl \
        mariadb-connector-c \
        tk
COPY --chown=www-data:www-data --from=build /root/.local /home/www-data/.local
COPY --chown=www-data:www-data ./app /app
COPY --chown=www-data:www-data gunicorn.conf.py /app
COPY --chown=www-data:www-data /app/credentials.prod.py /app/credentials.py
WORKDIR /app
USER www-data
ENV PATH=/home/www-data/.local/bin:$PATH
ENV ENVIRONMENT=production MYSQL_HOST=mariadb MYSQL_PORT=3306
RUN python -m pip install --upgrade pip --no-cache-dir
EXPOSE 8080
CMD [ "gunicorn", "-c", "gunicorn.conf.py", "app:app" ]
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 CMD [ "curl", "-f", "localhost:8080/api/health" ]
