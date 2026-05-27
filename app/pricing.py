BTTF_FILMS = {
    "Back to the Future 1",
    "Back to the Future 2",
    "Back to the Future 3",
}

BTTF_UNIT_PRICE = 15.0
OTHER_UNIT_PRICE = 20.0

DISCOUNT_TIERS = {3: 0.20, 2: 0.10, 1: 0.00}


def calculate_price(films: list[str]) -> dict:
    """
    Calcule le prix total d'un panier de DVDs.

    Args:
        films: liste des noms de films (peut contenir des doublons)

    Returns:
        dict avec :
        - total (float)         : prix final arrondi à 2 décimales
        - bttf_count (int)      : nombre total de DVDs BTTF achetés
        - bttf_different (int)  : nombre de volets BTTF différents
        - discount_rate (float) : taux appliqué (0.0, 0.1 ou 0.2)
        - other_count (int)     : nombre de films non-BTTF

    Exemples:
        >>> calculate_price(["Back to the Future 1",
                             "Back to the Future 2",
                             "Back to the Future 3"])
        {"total": 36.0, "bttf_count": 3, "bttf_different": 3,
         "discount_rate": 0.2, "other_count": 0}

        >>> calculate_price(["Back to the Future 1",
                             "Back to the Future 2",
                             "Back to the Future 3",
                             "Back to the Future 2"])
        {"total": 48.0, "bttf_count": 4, "bttf_different": 3,
         "discount_rate": 0.2, "other_count": 0}
    """
    if not films:
        return {
            "total": 0.0,
            "bttf_count": 0,
            "bttf_different": 0,
            "discount_rate": 0.0,
            "other_count": 0,
        }

    bttf_items = [f for f in films if f in BTTF_FILMS]
    other_items = [f for f in films if f not in BTTF_FILMS]

    bttf_count = len(bttf_items)
    bttf_different = len(set(bttf_items))
    other_count = len(other_items)

    # min(..., 3) pour gérer d'éventuels cas > 3 défensively
    tier = min(bttf_different, 3)
    discount_rate = DISCOUNT_TIERS.get(tier, 0.0)

    bttf_total = bttf_count * BTTF_UNIT_PRICE * (1 - discount_rate)
    other_total = other_count * OTHER_UNIT_PRICE

    total = round(bttf_total + other_total, 2)

    return {
        "total": total,
        "bttf_count": bttf_count,
        "bttf_different": bttf_different,
        "discount_rate": discount_rate,
        "other_count": other_count,
    }
