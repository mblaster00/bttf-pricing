FROM python:3.12-slim

WORKDIR /app

# Copie uniquement pyproject.toml d'abord pour profiter du cache Docker
COPY pyproject.toml .

# Copie le code source
COPY app/ ./app/

# Install sans les dépendances dev
RUN pip install --no-cache-dir -e .

# Utilisateur non-root pour la sécurité
RUN useradd --create-home appuser
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
