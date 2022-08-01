from typing import List

from Command import Command


class MacroCommand(Command):
    commands: List[Command]
        
    def __init__(self, commands: List[Command]):
        self.commands = commands
        
    def execute(self) -> None:
        for i in range(len(self.commands)):
            self.commands[i].execute()
            
    # NOTE:  these commands have to be done backwards to ensure 
    # proper undo functionality
            
    def undo(self) -> None:
        for i in range(len(self.commands)):
            self.commands[i].undo()