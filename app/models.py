from pydantic import BaseModel


class CartInput(BaseModel):
    """
    Panier d'entrée.

    Exemple:
        {
            "films": [
                "Back to the Future 1",
                "Back to the Future 2",
                "La chèvre"
            ]
        }
    """
    films: list[str]


class PriceDetail(BaseModel):
    """Détail du calcul retourné avec le prix final."""
    total: float
    bttf_count: int
    bttf_different: int
    discount_rate: float
    other_count: int


class PriceResult(BaseModel):
    """Réponse complète de l'API."""
    total: float
    detail: PriceDetail
