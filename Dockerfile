ARG SMOKE_BASE_IMAGE
FROM ${SMOKE_BASE_IMAGE}

WORKDIR /workspace/smoke_repo
COPY src ./src
COPY tests ./tests

CMD ["python3", "-m", "unittest", "discover", "-s", "tests"]
