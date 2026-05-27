from app.pricing import calculate_price


class TestExamplesEnonce:
    """Les 5 exemples exacts de l'énoncé — ces tests ne doivent jamais échouer."""

    def test_exemple_1_trois_volets_differents(self):
        films = ["Back to the Future 1", "Back to the Future 2", "Back to the Future 3"]
        result = calculate_price(films)
        assert result["total"] == 36.0
        assert result["bttf_different"] == 3
        assert result["discount_rate"] == 0.20

    def test_exemple_2_deux_volets_differents(self):
        films = ["Back to the Future 1", "Back to the Future 3"]
        result = calculate_price(films)
        assert result["total"] == 27.0
        assert result["bttf_different"] == 2
        assert result["discount_rate"] == 0.10

    def test_exemple_3_un_seul_volet(self):
        films = ["Back to the Future 1"]
        result = calculate_price(films)
        assert result["total"] == 15.0
        assert result["discount_rate"] == 0.0

    def test_exemple_4_trois_volets_avec_doublon(self):
        films = [
            "Back to the Future 1",
            "Back to the Future 2",
            "Back to the Future 3",
            "Back to the Future 2",
        ]
        result = calculate_price(films)
        assert result["total"] == 48.0
        assert result["bttf_count"] == 4
        assert result["bttf_different"] == 3
        assert result["discount_rate"] == 0.20

    def test_exemple_5_bttf_et_autre_film(self):
        films = [
            "Back to the Future 1",
            "Back to the Future 2",
            "Back to the Future 3",
            "La chèvre",
        ]
        result = calculate_price(films)
        assert result["total"] == 56.0
        assert result["other_count"] == 1


class TestCasLimites:
    """Cas limites pour robustesse."""

    def test_panier_vide(self):
        result = calculate_price([])
        assert result["total"] == 0.0

    def test_uniquement_autres_films(self):
        result = calculate_price(["La chèvre", "Titanic"])
        assert result["total"] == 40.0
        assert result["bttf_count"] == 0
        assert result["discount_rate"] == 0.0

    def test_casse_stricte_pas_de_reduction(self):
        # "back to the future 1" en minuscule != "Back to the Future 1"
        # donc compté comme autre film à 20€
        films = ["back to the future 1", "back to the future 2"]
        result = calculate_price(films)
        assert result["bttf_count"] == 0
        assert result["total"] == 40.0

    def test_plusieurs_exemplaires_meme_volet_sans_reduction(self):
        # Deux fois le même volet → 1 volet différent → 0% réduction
        films = ["Back to the Future 1", "Back to the Future 1"]
        result = calculate_price(films)
        assert result["bttf_count"] == 2
        assert result["bttf_different"] == 1
        assert result["discount_rate"] == 0.0
        assert result["total"] == 30.0
