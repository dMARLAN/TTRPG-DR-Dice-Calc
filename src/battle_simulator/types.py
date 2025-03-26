from dataclasses import dataclass

from color import Color


@dataclass(frozen=True)
class BattleSimulatorResult:
    hits: int
    misses: int
    damage_dealt: int

    def __str__(self):
        return (
            f"{Color.YELLOW}"
            f"Hits: {self.hits:,} "
            f"| Misses: {self.misses:,} "
            f"| Damage Dealt: {self.damage_dealt:,}"
            f"{Color.RESET}"
        )
