from typing import List

from Command import Command


def do_nothing(): pass

class SimpleRemoteControl:
    slot: Command = Command()
    
    def __init__(self):
        pass
    
    def setCommand(self, command: Command) -> None:
        self.slot = command
        
    def buttonWasPressed(self) -> None:
        self.slot.execute()