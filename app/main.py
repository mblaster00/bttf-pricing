import logging
import uuid

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.models import CartInput, PriceDetail, PriceResult
from app.pricing import calculate_price

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="BTTF Pricing API",
    description="""
Calcule le prix d'un panier de DVDs Back to the Future.

## Règles tarifaires

- DVD Back to the Future : **15€**
- 2 volets différents BTTF → **10% de réduction** sur tous les BTTF
- 3 volets différents BTTF → **20% de réduction** sur tous les BTTF
- Autres films : **20€**, sans réduction
    """,
    version="0.1.0",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
def index() -> FileResponse:
    """Sert l'interface web."""
    return FileResponse("app/static/index.html")


@app.get("/health")
def health() -> dict:
    """Vérifie que l'API est opérationnelle."""
    return {"status": "ok"}


@app.post("/calculate", response_model=PriceResult)
def calculate(cart: CartInput) -> PriceResult:
    """
    Calcule le prix total d'un panier de DVDs.

    Le panier est une liste de noms de films.
    Les noms sont sensibles à la casse.
    """
    request_id = str(uuid.uuid4())
    logger.info(
        f"[{request_id}] calculate called with {len(cart.films)} films"
    )

    result = calculate_price(cart.films)

    logger.info(
        f"[{request_id}] total={result['total']} "
        f"discount={result['discount_rate']}"
    )

    return PriceResult(
        total=result["total"],
        detail=PriceDetail(**result),
    )
