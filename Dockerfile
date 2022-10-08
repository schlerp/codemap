FROM ubuntu:latest as builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3 \
    python3-venv \
    python3-dev \
    python3-pip

RUN python3 -m venv /venv
ENV PATH="$VENV_PATH/bin:$PATH"

COPY requirements.txt .
RUN pip3 install -r requirements.txt

# final stage
FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /venv /venv

ENV PATH="/venv/bin:$PATH" \
    APP_USER=codemap

WORKDIR /app

RUN addgroup --gid 1001 --system $APP_USER && \
    adduser --no-create-home --shell /bin/false --disabled-password --uid 1001 --system --group $APP_USER

USER $APP_USER

COPY src/codemap/ /app/codemap
COPY scripts/docker_entrypoint /
ENTRYPOINT [ "/docker_entrypoint" ]
CMD [ "api" ]
