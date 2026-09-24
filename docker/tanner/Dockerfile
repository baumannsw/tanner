# syntax=docker/dockerfile:1

FROM python:3.11-alpine3.20

WORKDIR /opt/tanner

RUN <<'EOF'
apk -U --no-cache add \
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
EOF


COPY requirements.txt .

RUN <<'EOF'
python3 -m venv .venv
.venv/bin/python -m pip install --no-cache-dir --upgrade pip setuptools "Cython>=3.0"
.venv/bin/python -m pip install --no-cache-dir --no-build-isolation pylibinjection
.venv/bin/python -m pip install --no-cache-dir -r requirements.txt
EOF

COPY . .


RUN <<'EOF'
mv tanner/* .
.venv/bin/python setup.py install

EOF

# chown -R nobody:nobody /opt/tanner
# apk del --purge build-base linux-headers python3-dev
# rm -rf /root/* /tmp/* /var/tmp/* /var/cache/apk/*

# Start tanner
USER nobody:nobody
WORKDIR /opt/tanner
CMD ["tanner", "--config", "./data/config.yaml"]

