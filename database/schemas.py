def individual_data(player):
    return {
        "id": str(player["_id"]),
        "position": player["position"],
        "number": player["number"],
        "firstname": player["firstname"],
        "surname": player["surname"],
        "placebirth": player["placebirth"],
        "datebirth": player["datebirth"],
        "weight": player["weight"],
        "height": player["height"]
    }

def all_players(players):
    return [individual_data(player) for player in players]