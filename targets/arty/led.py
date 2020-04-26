# Flashing diodes for Digilent Arty Board

from migen import *
from migen.genlib.resetsync import AsyncResetSynchronizer

from litex.build.generic_platform import *

from litex.soc.cores.gpio import GPIOOut

from targets.arty.base import BaseSoC


class LEDSoC(BaseSoC):

    def __init__(self, platform, spiflash="spiflash_1x", **kwargs):
        BaseSoC.__init__(self, platform, spiflash, **kwargs)
        led = platform.request("rgb_leds")
        self.submodules.rgb_led_red = GPIOOut(led.r)
        self.submodules.rgb_led_green = GPIOOut(led.g) 
        self.submodules.rgb_led_blue = GPIOOut(led.b)
        self.add_csr("rgb_led_red")
        self.add_csr("rgb_led_green")
        self.add_csr("rgb_led_blue")
SoC = LEDSoC
