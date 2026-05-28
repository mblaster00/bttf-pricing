# BTTF Pricing

Web API for calculating Back to the Future DVD bundle pricing.

![CI](https://github.com/mblaster00/bttf-pricing/actions/workflows/ci.yml/badge.svg)

## Requirements
- Python 3.12+

## Setup

```bash
git clone https://github.com/mblaster00/bttf-pricing.git
cd bttf-pricing
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
make install
```

## Run

```bash
make run
```

- API : http://localhost:8000
- Swagger UI : http://localhost:8000/docs

## Test

```bash
make test
```

## Docker

```bash
# Build
make docker-build

# Run
make docker-run
```

API available at http://localhost:8000

## Web Interface

Open http://localhost:8000 in your browser.

Enter film names (one per line) and click Calculate.

## Lint

```bash
make lint
```

## API

### POST /calculate

Calcule le prix total d'un panier de DVDs.

**Request**
```json
{
  "films": [
    "Back to the Future 1",
    "Back to the Future 2",
    "Back to the Future 3"
  ]
}
```

**Response**
```json
{
  "total": 36.0,
  "detail": {
    "total": 36.0,
    "bttf_count": 3,
    "bttf_different": 3,
    "discount_rate": 0.2,
    "other_count": 0
  }
}
```

### GET /health

```json
{"status": "ok"}
```

## Pricing rules

| Condition | Discount |
|-----------|----------|
| 1 different BTTF volume | 0% |
| 2 different BTTF volumes | 10% off all BTTF DVDs |
| 3 different BTTF volumes | 20% off all BTTF DVDs |
| Other films | 20€ each, no discount |

Film names are case-sensitive.

## Project structure

```
bttf-pricing/
├── .github/
│   ├── workflows/
│   │   └── ci.yml                   # CI — pytest + ruff on every PR
│   └── pull_request_template.md     # PR checklist
├── app/
│   ├── static/
│   │   └── index.html               # Web interface (+/- cart)
│   ├── main.py                      # FastAPI — routes + static files
│   ├── models.py                    # Pydantic — CartInput, PriceResult
│   └── pricing.py                   # Business logic — pure function
├── tests/
│   └── test_pricing.py              # 9 tests — spec examples + edge cases
├── Dockerfile                       # Production image — python:3.12-slim
├── .dockerignore
├── Makefile                         # install, run, test, lint, docker-*
└── pyproject.toml                   # dependencies + build config
```
