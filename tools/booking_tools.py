import json
from langchain.tools import tool

@tool
def book_ticket(ticket_type: str, item_id: str, seat_or_seat_count: str, customer_email: str) -> str:
    """Réserve un billet (match, train ou avion) en mettant à jour le statut dans la base de données.
    Args:
        ticket_type: 'stadium', 'train' ou 'flight'
        item_id: L'identifiant unique (ex: 'ST-01', 'TR-101', 'FL-201')
        seat_or_seat_count: L'ID du siège (pour le stade ex: 'A12') ou le nombre de places (train/avion ex: '1')
        customer_email: L'adresse e-mail de confirmation de l'utilisateur
    """
    file_map = {
        "stadium": "data/stadium_tickets.json",
        "train": "data/train_tickets.json",
        "flight": "data/flight_tickets.json"
    }
    
    if ticket_type not in file_map:
        return "Type de billet invalide. Choisissez 'stadium', 'train' ou 'flight'."

    file_path = file_map[ticket_type]

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        found = False

        if ticket_type == "stadium":
            for match in data:
                if match["match_id"] == item_id:
                    for seat in match["seats"]:
                        if seat["seat_id"] == seat_or_seat_count and seat["status"] == "available":
                            seat["status"] = "booked"
                            found = True
                            break
        else:
            for item in data:
                id_key = "train_id" if ticket_type == "train" else "flight_id"
                if item[id_key] == item_id and item["available_seats"] > 0:
                    item["available_seats"] -= 1
                    found = True
                    break

        if found:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return f"SUCCÈS : La réservation ({ticket_type} ID: {item_id}) est confirmée ! Un e-mail de confirmation a été envoyé à {customer_email}."
        else:
            return f"ÉCHEC : Le billet {item_id} n'est plus disponible ou l'identifiant est incorrect."

    except Exception as e:
        return f"Erreur lors de la réservation : {str(e)}"