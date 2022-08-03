from Command import Command


class SimpleRemoteControl:
    slot: Command
    
    def __init__(self):
        pass
    
    def setCommand(self, command: Command) -> None:
        self.slot = command
        
    def buttonWasPressed(self) -> None:
        self.slot.execute()