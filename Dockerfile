
FROM python:3.11.3-buster

WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python" "-V"]
