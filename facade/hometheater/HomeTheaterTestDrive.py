from Amplifier import Amplifier
from CdPlayer import CdPlayer
from PopcornPopper import PopcornPopper
from Projector import Projector
from HomeTheaterFacade import HomeTheaterFacade
from Screen import Screen
from StreamingPlayer import StreamingPlayer
from TheaterLights import TheaterLights
from Tuner import Tuner


class HomeTheaterTestDrive:
    @staticmethod
    def main(*args):
        amp: Amplifier = Amplifier('Amplifier')
        tuner: Tuner = Tuner("AM/FM Tuner", amp)
        player: StreamingPlayer = StreamingPlayer("Streaming Player", amp)
        cd: CdPlayer = CdPlayer("CD Player", amp)
        projector: Projector = Projector("Projector", player)
        lights: TheaterLights = TheaterLights("Theater Ceiling Lights")
        screen: Screen = Screen("Theater Screen")
        popper: PopcornPopper = PopcornPopper("Popcorn Popper")
            
        homeTheater: HomeTheaterFacade = HomeTheaterFacade(amp, tuner, player, \
                                                           projector, screen, lights, popper)
        
        homeTheater.watchMovie("Raiders of the Lost Ark")
        homeTheater.endMovie()
        
if __name__ == "__main__":
    HomeTheaterTestDrive.main()