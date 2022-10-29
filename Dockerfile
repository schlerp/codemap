FROM ubuntu:latest as base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TZ=Etc/UTC

# set
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    && echo 'APT::Install-Suggests "0";' >> /etc/apt/apt.conf.d/00-docker \
    && echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/00-docker \
    && DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get install -y \
    python3 \
    && rm -rf /var/lib/apt/lists/*

FROM base as builder

RUN DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libgeos-dev \
    python3-venv \
    python3-dev \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /venv

COPY requirements.txt .
RUN . /venv/bin/activate && pip3 install -r requirements.txt

# final stage
FROM base as runner

RUN apt-get update && apt-get install -y \
    python3 \
    && rm -rf /var/lib/apt/lists/*

ENV APP_USER=codemap

RUN addgroup --gid 1001 --system $APP_USER && \
    adduser --home /app --shell /bin/false --disabled-password --uid 1001 --system --group $APP_USER

USER $APP_USER

COPY --from=builder /venv /venv

ENV PATH="/venv/bin:$PATH"

COPY src/codemap/ /app/codemap
COPY scripts/docker_entrypoint /usr/local/bin/

WORKDIR /app

ENTRYPOINT [ "/usr/local/bin/docker_entrypoint" ]
CMD [ "api" ]
