from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import FIRE, FIRE_TYPE


class Fire(PowerUp):
    def __init__(self):
        super().__init__(FIRE, FIRE_TYPE)