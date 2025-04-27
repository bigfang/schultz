FROM python:3.12-slim AS builder

ENV UV_LINK_MODE=copy
ENV UV_COMPILE_BYTECODE=1

COPY --from=ghcr.io/astral-sh/uv:0.7.5 /uv /uvx /bin/

WORKDIR /app

COPY . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-editable


FROM python:3.12-slim AS app

WORKDIR /app

RUN	set -eux; \
    groupadd -r appuser; \
    useradd -r -g appuser appuser

COPY --from=builder --chown=appuser:appuser /app /app

USER appuser

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
