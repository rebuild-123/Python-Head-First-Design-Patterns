class Stereo:
    location: str
        
    def __init__(self, location: str):
        self.location = location
        
    def on(self) -> None:
        print(f'{self.location} stereo is on')
        
    def off(self) -> None:
        print(f'{self.location} stereo is off')
        
    def setCD(self) -> None:
        print(f'{self.location} stereo is set for CD input')
        
    def setDVD(self) -> None:
        print(f'{self.location} stereo is set for DVD input')
        
    def setRadio(self) -> None:
        print(f'{self.location} stereo is set for Radio')
        
    def setVolume(self, volume: int) -> None:
        # code to set the volume
        # valid range: 1-11 (after all 11 is better than 10, right?)
        print(f'{self.location} stereo volume set to {volume}')