FROM ubuntu:latest

LABEL maintainer="stureiko@gmail.com"
LABEL version="1.0"
LABEL description="First simple docker image"

COPY ./test.sh /

RUN chmod a+x /test.sh

CMD "/test.sh"