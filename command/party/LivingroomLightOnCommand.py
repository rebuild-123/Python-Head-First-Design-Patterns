from Command import Command
from Light import Light


class LivingroomLightOnCommand(Command):
    light: Light
        
    def __init__(self, light: Light):
        self.light = light
        
    def execute(self) -> None:
        self.light.on()
        
    def undo(self) -> None:
        self.light.off()