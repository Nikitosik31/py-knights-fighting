
class Knight:
    def __init__(self, name, base_hp, base_power, armour, weapon, potion ):
        self.name = name
        self.base_hp = base_hp
        self.base_power = base_power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def get_stats(self) -> dict:
    # считаешь hp, power, protection
        armour = sum(
            arm["protection"] for arm in self.armour or []
        )
        power = self.base_power
        hp = self.base_hp
        protection = armour
        power += self.weapon["power"] if self.weapon else 0

        if self.potion:
            effect = self.potion["effect"]
            hp += effect.get("hp", 0)
            protection += effect.get("protection", 0)
            power += effect.get("power", 0)

        return {
            "hp": hp,
            "power": power,
            "protection": protection
        }


data = KNIGHTS["red_knight"]
Knight(
    name=data["name"],
    base_hp=data["hp"],
    base_power=data["power"],
    armour=data["armour"],
    weapon=data["weapon"],
    potion=data["potion"]
)
