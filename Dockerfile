# 1. Swap from Debian to Alpine Linux
FROM python:3.11-alpine

WORKDIR /app

# 2. Alpine uses 'apk' instead of 'apt-get'
RUN apk update && apk upgrade --no-cache

# 3. Upgrade core Python tools (optional but good practice)
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# 4. Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your code and run
COPY . .
CMD ["python", "app.py"]
