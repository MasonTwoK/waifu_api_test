FROM python:latest

COPY . /usr/src/waifu_api_test

WORKDIR /usr/src/waifu_api_test

RUN cat /usr/src/waifu_api_test/.env
RUN pip install -r requirements.txt

CMD ["pytest", "-v", "/usr/src/waifu_api_test"]
