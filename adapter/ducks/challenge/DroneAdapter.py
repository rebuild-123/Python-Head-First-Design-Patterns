from .Drone import Drone
from Duck import Duck


class DroneAdapter(Duck):
    drone: Drone
        
    def __init__(self, drone: Drone):
        self.drone = drone
        
    def quack(self) -> None:
        self.drone.beep()
        
    def fly(self) -> None:
        self.drone.spin_rotors()
        self.drone.take_off()