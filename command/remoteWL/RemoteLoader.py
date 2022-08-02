from CeilingFan import CeilingFan
from Command import Command
from RemoteControl import RemoteControl
from GarageDoor import GarageDoor
from Light import Light
from Stereo import Stereo


class RemoteLoader:
    @staticmethod
    def main(*argw) -> None:
        remoteControl: RemoteControl = RemoteControl()
        
        livingRoomLight: Light = Light("Living Room")
        kitchenLight: Light = Light("Kitchen")
        ceilingFan: CeilingFan = CeilingFan("Living Room")
        garageDoor: GarageDoor = GarageDoor("Main house")
        stereo: Stereo = Stereo("Living Room")

        remoteControl.setCommand(0, lambda: livingRoomLight.on(), lambda: livingRoomLight.off())
        remoteControl.setCommand(1, lambda: kitchenLight.on(), lambda: kitchenLight.off())
        remoteControl.setCommand(2, lambda: ceilingFan.high(), lambda: ceilingFan.off())
        
        stereoOnWithCD: Command = lambda: (stereo.on(), stereo.setCD(), stereo.setVolume(11))
        remoteControl.setCommand(3, stereoOnWithCD, lambda: stereo.off())
        remoteControl.setCommand(4, lambda: garageDoor.up(), lambda: garageDoor.down())
        
        print(remoteControl.toString())
        
        remoteControl.onButtonWasPushed(0)
        remoteControl.offButtonWasPushed(0)
        remoteControl.onButtonWasPushed(1)
        remoteControl.offButtonWasPushed(1)
        remoteControl.onButtonWasPushed(2)
        remoteControl.offButtonWasPushed(2)
        remoteControl.onButtonWasPushed(3)
        remoteControl.offButtonWasPushed(3)
        
if __name__ == "__main__":
    RemoteLoader.main()