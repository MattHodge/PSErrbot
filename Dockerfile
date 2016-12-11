FROM python:3.5.2-alpine

COPY . /errbot 

RUN echo "===> Adding Python runtime..."  && \
    apk --update add git && \
    apk --update add --virtual build-dependencies \
        openssl ca-certificates openssl-dev libffi-dev build-base  && \
    \
    \
    echo "===> Installing pip packages..."  && \
    cd /errbot                         && \
    pip install -r requirements.txt         && \
    \
    \    
    echo "===> Removing package list..."  && \
    apk del build-dependencies            && \
    rm -rf /var/cache/apk/*

WORKDIR /errbot

CMD [ "errbot" ]
