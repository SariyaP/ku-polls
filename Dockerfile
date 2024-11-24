FROM python:3-alpine
#ARG SECRET_KEY=secret_key
#ARG ALLOWED_HOSTS=127.0.0.1,localhost

WORKDIR /app/polls

## Set needed settings
#ENV SECRET_KEY=${SECRET_KEY}
#ENV DEBUG=True
#ENV TIMEZONE=Asia/Bangkok
#ENV ALLOWED_HOSTS=${ALLOWED_HOSTS:-127.0.0.1,localhost}

# Install dependency in Docker container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x ./entrypoint.sh

EXPOSE 8000
# Run application
CMD [ "./entrypoint.sh" ]
