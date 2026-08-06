ARG SMOKE_BASE_IMAGE=benchmark/pandas-baseline:prewarm
FROM ${SMOKE_BASE_IMAGE}

WORKDIR /workspace/smoke_repo
COPY . /workspace/smoke_repo
