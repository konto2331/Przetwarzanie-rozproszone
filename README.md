# Przetwarzanie-rozproszone
Lab2

 System Rozproszony – Mikroserwisy FastAPI

To jest prosty przykład systemu rozproszonego składającego się z dwóch mikroserwisów w Pythonie:
1. Serwis Produktów (`product_service.py`) – udostępnia informacje o produktach (port 8001).  
2. Serwis Magazynowy (`stock_service.py`) – podaje stan magazynowy produktów, odpyta produkt_service, aby sprawdzić, czy produkt istnieje (port 8002).
 Wymagania
•	- Python ≥ 3.7
•	- Pip
•	- (Opcjonalnie) curl do testów w terminalu

Instrukcja uruchomienia
1. Sklonuj repozytorium i przejdź do folderu projektu:
git clone <URL_REPO>
cd system rozproszony
2. Utwórz i aktywuj wirtualne środowisko
Na Windows:
python -m venv venv
.\venv\Scripts\activate
3. Zainstaluj wymagane biblioteki:
pip install fastapi "uvicorn[standard]" requests
4. Uruchom Serwis Produktów (port 8001):
uvicorn product_service:app --host 0.0.0.0 --port 8001
5. Uruchom Serwis Magazynowy (port 8002) w nowym terminalu:
uvicorn stock_service:app --host 0.0.0.0 --port 8002


Testowanie
1.	Produkt istnieje i jest w magazynie
curl http://localhost:8002/stock/2
Oczekiwany wynik:
{"productId":2,"quantity":150}
2.	Produkt nie istnieje
curl -i http://localhost:8002/stock/99
Oczekiwany wynik:
{"detail":"Produkt nie został znaleziony."}
3.	Produkt istnieje, ale brak stanu magazynowego
curl -i http://localhost:8002/stock/3
Oczekiwany wynik:
{"detail":"Brak informacji o stanie magazynowym dla produktu ID 3."}

Struktura projektu
Przetwarzanie-rozproszone/
│
├── product_service.py
├── stock_service.py
├── README.md
└── venv/     # wirtualne środowisko

