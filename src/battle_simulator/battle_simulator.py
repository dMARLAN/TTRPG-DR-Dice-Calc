from battle_simulator.types import BattleSimulatorResult
from ttrpg_types import Attack, Damage, Defense


class BattleSimulator:
    def __init__(
        self,
        attack: Attack,
        damage: Damage,
        defense: Defense,
        rounds: int,
    ):
        self.__attack = attack
        self.__damage = damage
        self.__defense = defense
        self.__rounds = rounds

    def run(self) -> BattleSimulatorResult:
        damage_dealt = 0
        hits = 0
        misses = 0

        for _ in range(self.__rounds):
            attack = self.__attack.roll()

            if attack.result >= self.__defense.armor_class or attack.is_nat_20():
                damage = self.__damage.roll()
                if attack.is_nat_20():
                    damage *= 2

                damage_dealt += max((damage - self.__defense.damage_reduction), 0)
                hits += 1
            else:
                misses += 1

        return BattleSimulatorResult(
            hits=hits,
            misses=misses,
            damage_dealt=damage_dealt,
        )
