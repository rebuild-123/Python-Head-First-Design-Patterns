from Command import Command
from GarageDoor import GarageDoor


class GarageDoorDownCommand(Command):
    garageDoor: GarageDoor
    
    def __init__(self, garageDoor: GarageDoor):
        self.garageDoor = garageDoor
        
    def execute(self) -> None:
        # self.garageDoor.up()
        self.garageDoor.down()