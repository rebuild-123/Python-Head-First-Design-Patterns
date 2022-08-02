from typing import List

from Command import Command


def do_nothing(): pass

class RemoteControl:
    def __init__(self):
        self.onCommands: List[Command] = [Command() for _ in range(7)]
        for i,descriptor in enumerate(self.onCommands): descriptor.__set_name__(RemoteControl, f'_onCommands__{i}')
        self.offCommands: List[Command] = [Command() for _ in range(7)]
        for i,descriptor in enumerate(self.offCommands): descriptor.__set_name__(RemoteControl, f'_offCommands__{i}')
        
        for i in range(7):
            # self.onCommands[i] = lambda: pass # lambda: pass is invalid syntax
            # self.offCommands[i] = lambda: pass # lambda: pass is invalid syntax
            self.onCommands[i].__set__(self, do_nothing)
            self.offCommands[i].__set__(self, do_nothing)
    
    def setCommand(self, slot: int, onCommand: Command, offCommand: Command) -> None:
        self.onCommands[slot].__set__(self, onCommand)
        self.offCommands[slot].__set__(self, offCommand)
        
    def onButtonWasPushed(self, slot: int) -> None:
        self.onCommands[slot].__get__(self, RemoteControl).execute()
        
    def offButtonWasPushed(self, slot: int) -> None:
        self.offCommands[slot].__get__(self, RemoteControl).execute()
        
    def toString(self) -> str:
        stringBuff: StringBuffer = StringBuffer()
        stringBuff.append("\n------ Remote Control -------\n")
        for i in range(len(self.onCommands)):
            stringBuff.append(f"[slot {i}] {self.onCommands[i].__name__:25s}{self.offCommands[i].__name__}\n")
        return stringBuff.toString()
        
class StringBuffer:
    def __init__(self):
        self.ls = []
        
    def append(self, string: str) -> None:
        self.ls.append(string)
        
    def toString(self) -> str:
        return ''.join(self.ls)