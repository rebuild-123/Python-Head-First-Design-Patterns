from typing import List

from Command import Command
from NoCommand import NoCommand


class RemoteControl:
    onCommands: List[Command]
    offCommands: List[Command]
    undoCommand: Command
    
    def __init__(self):
        self.onCommands = [None]*7
        self.offCommands = [None]*7
        noCommand: Command = NoCommand()
        for i in range(7):
            self.onCommands[i] = noCommand
            self.offCommands[i] = noCommand
        self.undoCommand = noCommand
    
    def setCommand(self, slot: int, onCommand: Command, offCommand: Command) -> None:
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand
        
    def onButtonWasPushed(self, slot: int) -> None:
        self.onCommands[slot].execute()
        self.undoCommand = self.onCommands[slot]
        
    def offButtonWasPushed(self, slot: int) -> None:
        self.offCommands[slot].execute()
        self.undoCommand = self.offCommands[slot]
        
    def toString(self) -> str:
        stringBuff: StringBuffer = StringBuffer()
        stringBuff.append("\n------ Remote Control -------\n")
        for i in range(len(self.onCommands)):
            stringBuff.append(f"[slot {i}] {self.onCommands[i].__class__.__name__:25s}{self.offCommands[i].__class__.__name__}\n")
        stringBuff.append(f"[undo] {self.undoCommand.__class__.__name__}\n")
        return stringBuff.toString()
        
class StringBuffer:
    def __init__(self):
        self.ls = []
        
    def append(self, string: str) -> None:
        self.ls.append(string)
        
    def toString(self) -> str:
        return ''.join(self.ls)