from dataclasses import dataclass, field
import random


@dataclass(frozen=True)
class Die:
    sides: int

    def roll(self):
        return random.randint(1, self.sides)

    def __str__(self):
        return f"d{self.sides}"


@dataclass(frozen=True)
class Defense:
    armor_class: int
    damage_reduction: int

    def __str__(self):
        return f"Armor Class: {self.armor_class} | Damage Reduction: {self.damage_reduction}"


@dataclass(frozen=True)
class Damage:
    die_sides: int
    num_die: int
    bonus: int
    critical_multiplier: int = 2

    die: Die = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, 'die', Die(self.die_sides))

    def roll(self):
        return sum(self.die.roll() for _ in range(self.num_die)) + self.bonus

    def __str__(self):
        return f"Damage: {self.num_die}d{self.die_sides}+{self.bonus}"


@dataclass(frozen=True)
class AttackResult:
    roll: int
    bonus: int
    critical_threat_range: int = 20

    @property
    def result(self):
        return self.roll + self.bonus

    def is_nat_20(self):
        return self.roll == 20

    def is_critical_threat(self):
        return self.roll >= self.critical_threat_range


@dataclass(frozen=True)
class Attack:
    bonus: int
    critical_threat_range: int = 20

    die: Die = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, 'die', Die(20))

    def roll(self) -> AttackResult:
        return AttackResult(
            roll=self.die.roll(),
            bonus=self.bonus,
            critical_threat_range=self.critical_threat_range,
        )

    def __str__(self):
        return f"Attack: 1{self.die}+{self.bonus}"
