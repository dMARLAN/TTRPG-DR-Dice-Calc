from battle_simulator.types import BattleSimulatorResult
from ttrpg_types import Attack, Damage, Defense, AttackResult


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

    def __is_critical_hit(self, attack: AttackResult) -> bool:
        if attack.is_critical_threat():
            confirm_attack = self.__attack.roll()
            if confirm_attack.result >= self.__defense.armor_class or confirm_attack.is_nat_20():
                return True
        return False

    def run(self) -> BattleSimulatorResult:
        damage_dealt = 0
        hits = 0
        misses = 0

        for _ in range(self.__rounds):
            attack = self.__attack.roll()

            if attack.result >= self.__defense.armor_class or attack.is_nat_20():
                if self.__is_critical_hit(attack):
                    damage = sum(self.__damage.roll() for _ in range(self.__damage.critical_multiplier))
                else:
                    damage = self.__damage.roll()

                damage_dealt += max((damage - self.__defense.damage_reduction), 0)
                hits += 1
            else:
                misses += 1

        return BattleSimulatorResult(
            hits=hits,
            misses=misses,
            damage_dealt=damage_dealt,
        )
