from app.KNIGHTS_list.knight import Knight

def battle(knight1: Knight, knight2: Knight) -> dict:
    stats1 = knight1.get_stats()
    stats2 = knight2.get_stats()

    damage_to_1 = stats2["power"] - stats1["protection"]
    damage_to_2 = stats1["power"] - stats2["protection"]

    stats1["hp"] -= damage_to_1
    stats2["hp"] -= damage_to_2
    if stats1["hp"] <= 0:
        stats1["hp"] = 0
    if stats2["hp"] <= 0:
        stats2["hp"] = 0

    return {
        knight1.name: stats1["hp"],
        knight2.name: stats2["hp"]
    }
