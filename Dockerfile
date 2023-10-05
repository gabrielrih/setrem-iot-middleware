FROM python:3.11.4-bullseye
WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt
COPY ./src src
COPY ./app.py app.py
CMD ["python", "app.py"]
EXPOSE 5683/udp