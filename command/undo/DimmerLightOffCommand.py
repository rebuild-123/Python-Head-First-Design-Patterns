from Command import Command
from Light import Light


class DimmerLightOffCommand(Command):
    light: Light
    prevLevel: int = 0
        
    def __init__(self, light: Light):
        self.light = light
        self.prevLevel = 100
        
    def execute(self) -> None:
        self.prevLevel = self.light.getLevel()
        self.light.off()
        
    def undo(self) -> None:
        self.light.dim(self.prevLevel)