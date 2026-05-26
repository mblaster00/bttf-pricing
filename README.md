# BTTF Pricing

Web API for calculating Back to the Future DVD bundle pricing.

## Requirements
- Python 3.12+

## Setup

```bash
git clone <repo>
cd bttf-pricing
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
make install
```

## Run

```bash
make run
```

API available at http://localhost:8000
Interactive docs at http://localhost:8000/docs

## Test

```bash
make test
```

## Pricing rules

- Any DVD: 15€
- 2 different BTTF volumes: 10% off all BTTF DVDs
- 3 different BTTF volumes: 20% off all BTTF DVDs
- Other films: 20€ each, no discount
