FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install flask requests python-dotenv

EXPOSE 5000

CMD ["python", "webhook_server.py"]