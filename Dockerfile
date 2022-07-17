FROM python:3.6-slim
MAINTAINER Abdennour TOUMI <http://in.abdennoor.com>

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD python ./BookmarkServer.py
