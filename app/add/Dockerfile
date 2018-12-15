FROM alpine:3.8
MAINTAINER Rehan Anwar <rehanann@gmail.com>

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

RUN pip3 install flask
RUN pip3 install flask_restful
RUN mkdir -p /opt/python
COPY app.py /opt/python
ENV FLASK_APP=app.py
EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD [ "/opt/python/app.py" ]
