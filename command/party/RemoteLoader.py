from typing import List

from Command import Command
from RemoteControl import RemoteControl
from Hottub import Hottub
from HottubOffCommand import HottubOffCommand
from HottubOnCommand import HottubOnCommand
from Light import Light
from LightOffCommand import LightOffCommand
from LightOnCommand import LightOnCommand
from MacroCommand import MacroCommand
from Stereo import Stereo
from StereoOffCommand import StereoOffCommand
from StereoOnCommand import StereoOnCommand
from TV import TV
from TVOffCommand import TVOffCommand
from TVOnCommand import TVOnCommand


class RemoteLoader:
    @staticmethod
    def main(*argw) -> None:
        remoteControl: RemoteControl = RemoteControl()
        
        light: Light = Light("Living Room")
        tv: TV = TV("Living Room")
        stereo: Stereo = Stereo("Living Room")
        hottub: Hottub = Hottub()

        lightOn: LightOnCommand = LightOnCommand(light)
        stereoOn: StereoOnCommand = StereoOnCommand(stereo)
        tvOn: TVOnCommand = TVOnCommand(tv)
        hottubOn: HottubOnCommand = HottubOnCommand(hottub)
        lightOff: LightOffCommand = LightOffCommand(light)
        stereoOff: StereoOffCommand = StereoOffCommand(stereo)
        tvOff: TVOffCommand = TVOffCommand(tv)
        hottubOff: HottubOffCommand = HottubOffCommand(hottub)
            
        partyOn: List[Command] = [lightOn, stereoOn, tvOn, hottubOn]
        partyOff: List[Command] = [lightOff, stereoOff, tvOff, hottubOff]
            
        partyOnMacro: MacroCommand = MacroCommand(partyOn)
        partyOffMacro: MacroCommand = MacroCommand(partyOff)
            
        remoteControl.setCommand(0, partyOnMacro, partyOffMacro)
        
        print(remoteControl.toString())
        print("--- Pushing Macro On---")
        remoteControl.onButtonWasPushed(0)
        print("--- Pushing Macro Off---")
        remoteControl.offButtonWasPushed(0)
        
if __name__ == "__main__":
    RemoteLoader.main()