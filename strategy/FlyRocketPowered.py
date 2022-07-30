from abc import ABC, abstractmethod

from FlyBehavior import FlyBehavior


class FlyRocketPowered(FlyBehavior):
    def fly(self) -> None:
        print("I'm flying with a rocket")