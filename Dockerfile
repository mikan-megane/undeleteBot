FROM python:3-slim

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
  ffmpeg \
  make \
  gcc libc-dev g++ \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip wheel
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "-u", "./startbot.py" ]