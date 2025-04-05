FROM python:3.12-slim-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

VOLUME /app/data

# Create and set the database path
RUN mkdir -p /app/data
ENV DATABASE_URL=sqlite:////app/data/database.db

EXPOSE 5000

CMD ["python", "app.py"]