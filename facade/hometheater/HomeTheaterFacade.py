from Amplifier import Amplifier
from CdPlayer import CdPlayer
from PopcornPopper import PopcornPopper
from Projector import Projector
from Screen import Screen
from StreamingPlayer import StreamingPlayer
from TheaterLights import TheaterLights
from Tuner import Tuner


class HomeTheaterFacade:
    amp: Amplifier
    tuner: Tuner
    player: StreamingPlayer
    cd: CdPlayer
    projector: Projector
    lights: TheaterLights
    screen: Screen
    popper: PopcornPopper
        
    def __init__(
        self, 
        amp: Amplifier,
        tuner: Tuner,
        player: StreamingPlayer,
        projector: Projector,
        screen: Screen,
        lights: TheaterLights,
        popper: PopcornPopper
    ):
        self.amp = amp
        self.tuner = tuner
        self.player = player
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper
        
    def watchMovie(self, movie: str) -> None:
        print("Get ready to watch a movie...")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wideScreenMode()
        self.amp.on()
        self.amp.setStreamingPlayer(self.player)
        self.amp.setSurroundSound()
        self.amp.setVolume(5)
        self.player.on()
        self.player.play(movie)
        
    def endMovie(self) -> None:
        print("Shutting movie theater down...")
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.player.stop()
        self.player.off()
        
    def listenToRadio(self, frequency: float) -> None:
        print("Tuning in the airwaves...")
        self.tuner.on()
        self.tuner.setFrequency(frequency)
        self.amp.on()
        self.amp.setVolume(5)
        self.amp.setTuner(self.tuner)
        
    def endRadio(self) -> None:
        print("Shutting down the tuner...")
        self.tuner.off()
        self.amp.off()