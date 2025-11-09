# product_service.py
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Serwis Produktów")

DB_PRODUCTS = {
    1: {"id": 1, "name": "Laptop Pro", "price": 5200.99},
    2: {"id": 2, "name": "Mysz bezprzewodowa", "price": 150.50},
    3: {"id": 3, "name": "Monitor 4K", "price": 1800.00},
}

@app.get("/products/{id}")
def get_product_by_id(id: int):
    """
    Funkcja obsługująca zapytanie o produkt.
    Przyjmuje 'id' jako argument (FastAPI automatycznie konwertuje go na liczbę).
    """
    # Używamy metody .get(), która bezpiecznie pobiera wartość ze słownika.
    # Jeśli klucz 'id' nie istnieje, zwróci None.
    product = DB_PRODUCTS.get(id)
    
    # Jeśli produkt nie został znaleziony, zwracamy błąd.
    if not product:
        # HTTPException to specjalny wyjątek FastAPI, który generuje
        # odpowiedź HTTP z kodem błędu i wiadomością w formacie JSON.
        raise HTTPException(status_code=404, detail="Product not found")
        
    # Jeśli produkt został znaleziony, zwracamy go. FastAPI automatycznie
    return product
