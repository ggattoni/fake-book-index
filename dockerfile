FROM ghcr.io/astral-sh/uv:python3.12-alpine

WORKDIR /app
COPY . .
RUN uv sync

CMD ["uv", "run", "fake-book-index"]