from app.fight import fight
from app.preparations import battle_preparation


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = battle_preparation(knights_config["lancelot"])

    # arthur
    arthur = battle_preparation(knights_config["arthur"])

    # mordred
    mordred = battle_preparation(knights_config["mordred"])

    # red_knight
    red_knight = battle_preparation(knights_config["red_knight"])

    # BATTLE:

    # 1 Lancelot vs Mordred:
    fight_1 = fight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    fight_2 = fight(arthur, red_knight)

    fight_1.update(fight_2)
    # Return battle results:
    return fight_1


print(battle)
