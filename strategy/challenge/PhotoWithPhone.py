import re
import sys

from BasicCameraApp import BasicCameraApp
from Email import Email
from PhoneCameraApp import PhoneCameraApp
from Social import Social
from Txt import Txt


class PhotoWithPhone:
    @staticmethod
    def main(*args):
        cameraApp: PhoneCameraApp = BasicCameraApp()
        share: str = PhotoWithPhone.getSharing()
        if re.match(r'3\.[1-9][0-9]\.', sys.version[:5]):
            # Only for python 3.10 and later
            match share:
                case "t": cameraApp.setShareStrategy(Txt())
                case "e": cameraApp.setShareStrategy(Email())
                case "s": cameraApp.setShareStrategy(Social())
                case _: cameraApp.setShareStrategy(Txt())
        else:
            if share == "t": cameraApp.setShareStrategy(Txt())
            elif share == "e": cameraApp.setShareStrategy(Email())
            elif share == "s": cameraApp.setShareStrategy(Social())
            else: cameraApp.setShareStrategy(Txt())
        cameraApp.take()
        cameraApp.edit()
        cameraApp.save()
        cameraApp.share()
            
    @staticmethod
    def getSharing() -> str:
        print("Share with txt (t), email (e), or social media (s)?")
        appName = input()
        return appName
    
if __name__ == "__main__":
    PhotoWithPhone.main()