from Command import Command
from Light import Light


class DimmerLightOnCommand(Command):
    light: Light
    prevLevel: int = 0
        
    def __init__(self, light: Light):
        self.light = light
        
    def execute(self) -> None:
        self.prevLevel = self.light.getLevel()
        self.light.dim(75)
        
    def undo(self) -> None:
        self.light.dim(self.prevLevel)