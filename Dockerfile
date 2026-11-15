# Headless Chromium for real-browser runs and screenshots (ADR-0003).
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    CHROME_BIN=/usr/bin/chromium \
    CHROMEDRIVER_PATH=/usr/bin/chromedriver

RUN apt-get update \
    && apt-get install -y --no-install-recommends chromium chromium-driver fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml README.md LICENSE ./
COPY src ./src
RUN python -m pip install --upgrade pip && python -m pip install -e ".[dev]"
COPY tests ./tests

# Run as a user without root rights; it owns /app, where relative screenshot paths are written.
RUN useradd --create-home --uid 1000 app \
    && chown app /app
USER app

ENTRYPOINT ["python", "-m", "cookie_clicker_bot"]
CMD ["--headless"]
