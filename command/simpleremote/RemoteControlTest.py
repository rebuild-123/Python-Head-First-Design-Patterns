from GarageDoor import GarageDoor
from GarageDoorOpenCommand import GarageDoorOpenCommand
from Light import Light
from LightOnCommand import LightOnCommand
from SimpleRemoteControl import SimpleRemoteControl


class RemoteControlTest:
    @staticmethod
    def main(*argw) -> None:
        remote: SimpleRemoteControl = SimpleRemoteControl()
        
        light: Light = Light()
        garageDoor: GarageDoor = GarageDoor()

        lightOn: LightOnCommand = LightOnCommand(light)
        garageOpen: GarageDoorOpenCommand = GarageDoorOpenCommand(garageDoor)

        remote.setCommand(lightOn)
        remote.buttonWasPressed()
        remote.setCommand(garageOpen)
        remote.buttonWasPressed()
        
if __name__ == "__main__":
    RemoteControlTest.main()