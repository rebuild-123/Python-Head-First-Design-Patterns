from CeilingFan import CeilingFan
from CeilingFanOnCommand import CeilingFanOnCommand
from CeilingFanOffCommand import CeilingFanOffCommand
from RemoteControl import RemoteControl
from GarageDoor import GarageDoor
from GarageDoorDownCommand import GarageDoorDownCommand
from GarageDoorUpCommand import GarageDoorUpCommand
from Light import Light
from LightOffCommand import LightOffCommand
from LightOnCommand import LightOnCommand
from Stereo import Stereo
from StereoOffCommand import StereoOffCommand
from StereoOnWithCDCommand import StereoOnWithCDCommand


class RemoteLoader:
    @staticmethod
    def main(*argw) -> None:
        remoteControl: RemoteControl = RemoteControl()
        
        livingRoomLight: Light = Light("Living Room")
        kitchenLight: Light = Light("Kitchen")
        ceilingFan: CeilingFan = CeilingFan("Living Room")
        garageDoor: GarageDoor = GarageDoor("Garage")
        stereo: Stereo = Stereo("Living Room")

        livingRoomLightOn: LightOnCommand = LightOnCommand(livingRoomLight)
        livingRoomLightOff: LightOffCommand = LightOffCommand(livingRoomLight)
        kitchenLightOn: LightOnCommand = LightOnCommand(kitchenLight)
        kitchenLightOff: LightOffCommand = LightOffCommand(kitchenLight)

        ceilingFanOn: CeilingFanOnCommand = CeilingFanOnCommand(ceilingFan)
        ceilingFanOff: CeilingFanOffCommand = CeilingFanOffCommand(ceilingFan)

        garageDoorUp: GarageDoorUpCommand = GarageDoorUpCommand(garageDoor)
        garageDoorDown: GarageDoorDownCommand = GarageDoorDownCommand(garageDoor)

        stereoOnWithCD: StereoOnWithCDCommand = StereoOnWithCDCommand(stereo)
        stereoOff: StereoOffCommand = StereoOffCommand(stereo)

        remoteControl.setCommand(0, livingRoomLightOn, livingRoomLightOff)
        remoteControl.setCommand(1, kitchenLightOn, kitchenLightOff)
        remoteControl.setCommand(2, ceilingFanOn, ceilingFanOff)
        remoteControl.setCommand(3, stereoOnWithCD, stereoOff)
        
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