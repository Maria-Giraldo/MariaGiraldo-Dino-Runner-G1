from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import WEAPON, WEAPON_TYPE


class Weapon(PowerUp):
    def __init__(self):
        super().__init__(WEAPON, WEAPON_TYPE)