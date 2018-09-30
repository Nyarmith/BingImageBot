FROM frolvlad/alpine-python3

VOLUME /opt/picBot/
WORKDIR /opt/picBot/

RUN pip install telepot pyyaml requests

ADD PicBot.py .
CMD python3 PicBot.py
