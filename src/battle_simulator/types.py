from dataclasses import dataclass


@dataclass(frozen=True)
class BattleSimulatorResult:
    hits: int
    misses: int
    damage_dealt: int

    def __str__(self):
        return f"Hits: {self.hits}, Misses: {self.misses}, Damage Dealt: {self.damage_dealt}"
