from Command import Command
from GarageDoor import GarageDoor
from Light import Light
from SimpleRemoteControl import SimpleRemoteControl


class RemoteControlTest:
    @staticmethod
    def main(*argw) -> None:
        remote: SimpleRemoteControl = SimpleRemoteControl()
        
        light: Light = Light()
        garageDoor: GarageDoor = GarageDoor()

        remote.setCommand(lambda: light.on())
        remote.buttonWasPressed()
        remote.setCommand(lambda: garageDoor.up())
        remote.buttonWasPressed()
        remote.setCommand(lambda: garageDoor.lightOn())
        remote.buttonWasPressed()
        remote.setCommand(lambda: garageDoor.lightOff())
        remote.buttonWasPressed()
        
if __name__ == "__main__":
    RemoteControlTest.main()