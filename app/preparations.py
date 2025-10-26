def battle_preparation(knight: dict) -> dict:

    # apply armour
    knight["protection"] = 0
    for armour in knight.get("armour"):
        if not armour.get("protection"):
            knight["protection"] = 0
        else:
            knight["protection"] += armour.get("protection")

    # apply weapon
    knight["power"] += knight.get("weapon").get("power")

    # apply potion if exist
    potion = knight.get("potion")

    if potion and "power" in potion.get("effect"):
        knight["power"] += knight.get("potion").get("effect").get("power")

    if potion and "hp" in potion.get("effect"):
        knight["hp"] += knight.get("potion").get("effect").get("hp")

    if potion and "protection" in potion.get("effect"):
        knight["protection"] += (
            knight.get("potion").
            get("effect").
            get("protection")
        )

    return knight
