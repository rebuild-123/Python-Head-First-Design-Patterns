from Command import Command
from Light import Light


class LightOnCommand(Command):
    light: Light
    level: int = 0
        
    def __init__(self, light: Light):
        self.light = light
        
    def execute(self) -> None:
        self.level = self.light.getLevel()
        self.light.on()
        
    def undo(self) -> None:
        self.light.dim(self.level)