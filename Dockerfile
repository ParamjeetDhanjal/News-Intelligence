FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

# Copy application code
COPY . .

# Ensure .env is present (in case it was ignored by git)
# Mini Deploy copies the context, so if it's in the repo folder, it should be here.

ENV PORT=8080
EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]
