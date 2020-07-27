FROM python:3.6

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

ADD watchtower-client.py /watchtower-client.py

ADD run /usr/bin/update

CMD update

