# stock_service.py
import requests  # Biblioteka do wykonywania zapytań HTTP
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Serwis Magazynowy")

PRODUCT_SERVICE_URL = "http://localhost:8001"

# "Fałszywa" baza danych stanów magazynowych.
# Celowo nie ma tu produktu o ID=3, aby przetestować jeden z przypadków.
DB_STOCK = {
    1: 25,
    2: 150,
}

@app.get("/stock/{product_id}")
def get_stock_by_product_id(product_id: int):
    """
    Główna logika biznesowa serwisu.
    """
    # Krok 1: Wykonaj zapytanie HTTP GET do Serwisu Produktów.
    # Celem jest sprawdzenie, czy produkt o danym ID w ogóle istnieje.
    # Używamy bloku try-except, aby obsłużyć sytuację, gdy Serwis Produktów jest niedostępny.
    try:
        product_response = requests.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}")
    except requests.ConnectionError:
        # Jeśli nie udało się połączyć, zwracamy błąd 503 (Usługa Niedostępna).
        raise HTTPException(status_code=503, detail="Serwis produktów jest niedostępny.")

    # Krok 2: Sprawdź odpowiedź z Serwisu Produktów.
    # Jeśli Serwis Produktów odpowiedział kodem 404, to znaczy, że produkt nie istnieje.
    # W takiej sytuacji nasz serwis również powinien zwrócić 404.
    if product_response.status_code == 404:
        raise HTTPException(status_code=404, detail="Produkt nie został znaleziony.")

    # Krok 3: Produkt istnieje, więc sprawdzamy jego stan w naszej "bazie".
    stock_quantity = DB_STOCK.get(product_id)
    
    # Krok 4: Sprawdź, czy mamy informację o stanie magazynowym.
    # Może się zdarzyć, że produkt istnieje, ale nie mamy go w magazynie.
    if stock_quantity is None:
        raise HTTPException(
            status_code=404, 
            detail=f"Brak informacji o stanie magazynowym dla produktu ID {product_id}."
        )
        
    # Krok 5: Jeśli wszystko się udało, zwróć pomyślną odpowiedź.
    return {"productId": product_id, "quantity": stock_quantity}
