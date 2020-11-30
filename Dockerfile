FROM python:3.8

MAINTAINER Linto Paul "lintopaul@gmail.com"

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /

ENTRYPOINT [ "python" ]

CMD [ "webapp.py" ]