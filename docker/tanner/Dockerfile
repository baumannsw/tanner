FROM alpine:3.15

# Include dist
ADD ./docker/tanner/dist/ /root/dist/

RUN apk -U --no-cache add \
        build-base \
        git \
        libcap \
        libffi-dev \
        libressl-dev \
        linux-headers \
        py3-yarl \
        python3 \
        python3-dev \
        py3-pip

COPY ./tanner /opt/tanner

RUN cp /root/dist/config.yaml /opt/tanner/tanner/data/ && \
    python3 -m venv /opt/tanner/tanner-env && \
    /opt/tanner/tanner-env/bin/pip install --upgrade pip && \
    /opt/tanner/tanner-env/bin/pip install --no-cache-dir wheel && \
    /opt/tanner/tanner-env/bin/pip install --no-cache-dir -r /opt/tanner/requirements.txt && \
    cd /opt/tanner && \
    /opt/tanner/tanner-env/bin/python setup.py install && \
    chown -R nobody:nobody /opt/tanner && \
    apk del --purge build-base linux-headers python3-dev && \
    rm -rf /root/* /tmp/* /var/tmp/* /var/cache/apk/*

# Start tanner
USER nobody:nobody
WORKDIR /opt/tanner
CMD ["/opt/tanner/tanner-env/bin/tanner", "--config", "/opt/tanner/tanner/data/config.yaml"]

