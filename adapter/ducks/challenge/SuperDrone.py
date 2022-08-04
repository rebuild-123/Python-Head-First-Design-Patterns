from .Drone import Drone


class SuperDrone(Drone):
    def beep(self) -> None:
        print("Beep beep beep")
        
    def spin_rotors(self) -> None:
        print("Rotors are spinning")
        
    def take_off(self) -> None:
        print("Taking off")