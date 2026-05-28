VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# ── Local ──────────────────────────────────────────────
$(VENV):
	python -m venv $(VENV)

install: $(VENV)
	$(PIP) install -e ".[dev]"

run: $(VENV)
	$(VENV)/bin/uvicorn app.main:app --reload

test: $(VENV)
	$(VENV)/bin/pytest -v

lint: $(VENV)
	$(VENV)/bin/ruff check app/ tests/

# ── Docker ─────────────────────────────────────────────
docker-build:
	docker build -t bttf-pricing .

docker-run:
	docker run -p 8000:8000 bttf-pricing

docker-test:
	docker build -t bttf-pricing . && \
	docker run --rm bttf-pricing python -m pytest

.PHONY: install run test lint docker-build docker-run docker-test
