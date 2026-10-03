import json
from langchain.tools import tool

@tool
def search_stadium_tickets(query: str = "", max_price: float = 300.0) -> str:
    """Recherche des places de match selon le nom de l'équipe, la ville ou la date, avec un prix max."""
    try:
        with open("data/stadium_tickets.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        results = []
        for match in data:
            match_str = f"{match['teams']} {match['city']} {match['date']}".lower()
            if query.lower() in match_str or not query:
                available = [s for s in match["seats"] if s["status"] == "available" and s["price"] <= max_price]
                if available:
                    results.append({
                        "match_id": match["match_id"],
                        "match": match["teams"],
                        "city": match["city"],
                        "date": match["date"],
                        "available_seats": available
                    })
        return json.dumps(results, ensure_ascii=False)
    except Exception as e:
        return f"Erreur lors de la recherche des billets de stade : {str(e)}"
