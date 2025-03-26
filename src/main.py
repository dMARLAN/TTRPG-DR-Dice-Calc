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
    armor_class: int = 15
    damage_reduction: int = 10

    __run_simulation(
        attack=Attack(bonus=bonus),
        damage=Damage(num_die=3, die_sides=4, bonus=bonus),
        defense=Defense(armor_class=armor_class, damage_reduction=damage_reduction),
        rounds=1_000_000
    )

    print()

    __run_simulation(
        attack=Attack(bonus=bonus),
        damage=Damage(num_die=1, die_sides=12, bonus=bonus),
        defense=Defense(armor_class=armor_class, damage_reduction=damage_reduction),
        rounds=1_000_000
    )


if __name__ == "__main__":
    __main()
