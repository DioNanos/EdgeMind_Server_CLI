FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

ENV FLASK_APP=app/main.py
# This is a dev server. For production, use a proper WSGI server like Gunicorn.
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# The API_KEY should be set during `docker run`, e.g., -e API_KEY="your-secret-key"
# This default key is for convenience and is insecure.
ENV API_KEY="default_secret_key_change_me"

EXPOSE 5000

CMD ["flask", "run"]
