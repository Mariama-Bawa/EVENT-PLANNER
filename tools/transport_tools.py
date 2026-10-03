import json
from langchain.tools import tool

@tool
def search_transport_options(user_city: str, destination_city: str, max_budget: float = 500.0) -> str:
    """Compare les billets de train et d'avion disponibles depuis la ville actuelle de l'utilisateur vers la ville du match."""
    results = {"trains": [], "flights": []}
    
    try:
        with open("data/train_tickets.json", "r", encoding="utf-8") as f:
            trains = json.load(f)
        results["trains"] = [
            t for t in trains 
            if t["departure_city"].lower() == user_city.lower() 
            and t["arrival_city"].lower() == destination_city.lower() 
            and t["price"] <= max_budget
        ]
    except Exception as e:
        results["train_error"] = str(e)

    try:
        with open("data/flight_tickets.json", "r", encoding="utf-8") as f:
            flights = json.load(f)
        results["flights"] = [
            fl for fl in flights 
            if fl["departure_city"].lower() == user_city.lower() 
            and fl["arrival_city"].lower() == destination_city.lower() 
            and fl["price"] <= max_budget
        ]
    except Exception as e:
        results["flight_error"] = str(e)

    return json.dumps(results, ensure_ascii=False)
