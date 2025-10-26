from app.fight import fight
from app.preparations import battle_preparation


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    knights_list = []
    for knight in knights_config:
        knights_config[knight] = battle_preparation(knights_config[knight])
        knights_list.append(knights_config[knight])

    # 1 Lancelot vs Mordred:
    fight_1 = fight(knights_list[0], knights_list[2])

    # 2 Arthur vs Red Knight:
    fight_2 = fight(knights_list[1], knights_list[3])

    fight_1.update(fight_2)
    # Return battle results:
    return fight_1
