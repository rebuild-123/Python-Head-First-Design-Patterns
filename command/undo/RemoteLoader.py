from Command import Command
from CeilingFan import CeilingFan
from CeilingFanHighCommand import CeilingFanHighCommand
from CeilingFanMediumCommand import CeilingFanMediumCommand
from CeilingFanOffCommand import CeilingFanOffCommand
from RemoteControlWithUndo import RemoteControlWithUndo
from Light import Light
from LightOffCommand import LightOffCommand
from LightOnCommand import LightOnCommand


class RemoteLoader:
    @staticmethod
    def main(*argw) -> None:
        remoteControl: RemoteControlWithUndo = RemoteControlWithUndo()
        
        livingRoomLight: Light = Light("Living Room")
        livingRoomLightOn: LightOnCommand = LightOnCommand(livingRoomLight)
        livingRoomLightOff: LightOffCommand = LightOffCommand(livingRoomLight)
            
        remoteControl.setCommand(0, livingRoomLightOn, livingRoomLightOff)

        remoteControl.onButtonWasPushed(0)
        remoteControl.offButtonWasPushed(0)
        print(remoteControl.toString())
        remoteControl.undoButtonWasPushed()
        remoteControl.offButtonWasPushed(0)
        remoteControl.onButtonWasPushed(0)
        print(remoteControl.toString())
        remoteControl.undoButtonWasPushed()
        
        ceilingFan: CeilingFan = CeilingFan("Living Room")
        ceilingFanMedium: CeilingFanMediumCommand = CeilingFanMediumCommand(ceilingFan)
        ceilingFanHigh: CeilingFanHighCommand = CeilingFanHighCommand(ceilingFan)
        ceilingFanOff: CeilingFanOffCommand = CeilingFanOffCommand(ceilingFan)
            
        remoteControl.setCommand(0, ceilingFanMedium, ceilingFanOff)
        remoteControl.setCommand(1, ceilingFanHigh, ceilingFanOff)
        
        remoteControl.onButtonWasPushed(0)
        remoteControl.offButtonWasPushed(0)
        print(remoteControl.toString())
        remoteControl.undoButtonWasPushed()
 
        remoteControl.onButtonWasPushed(1)
        print(remoteControl.toString())
        remoteControl.undoButtonWasPushed()
        
if __name__ == "__main__":
    RemoteLoader.main()