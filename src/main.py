from battle_simulator import BattleSimulator
from ttrpg_types import Attack, Damage, Defense


def __run_simulation(attack: Attack, damage: Damage, defense: Defense, rounds: int) -> None:
    result = BattleSimulator(
        attack=attack,
        damage=damage,
        defense=defense,
        rounds=rounds,
    ).run()

    print(attack, "|", damage)
    print(defense)
    print(result)


def __main() -> None:
    bonus: int = 5

    # Gargoyle: https://www.d20pfsrd.com/bestiary/monster-listings/monstrous-humanoids/gargoyle/
    armor_class: int = 16
    damage_reduction: int = 10

    # Great Sword
    __run_simulation(
        attack=Attack(bonus=bonus, critical_threat_range=19),
        damage=Damage(num_die=2, die_sides=6, bonus=bonus, critical_multiplier=2),
        defense=Defense(armor_class=armor_class, damage_reduction=damage_reduction),
        rounds=1_000_000
    )

    print()

    # Great Axe
    __run_simulation(
        attack=Attack(bonus=bonus, critical_threat_range=20),
        damage=Damage(num_die=1, die_sides=12, bonus=bonus, critical_multiplier=3),
        defense=Defense(armor_class=armor_class, damage_reduction=damage_reduction),
        rounds=1_000_000
    )


if __name__ == "__main__":
    __main()
