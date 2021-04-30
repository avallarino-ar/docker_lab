FROM python:3.7.8-alpine3.12

WORKDIR /usr/src/apirest

COPY . /usr/src/apirest

RUN pip3 install --upgrade pip
RUN pip3 --no-cache-dir install -r requirements.txt

CMD  ["python3", "src/app_demo.py"]