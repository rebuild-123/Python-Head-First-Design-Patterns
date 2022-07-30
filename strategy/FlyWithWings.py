from abc import ABC, abstractmethod

from FlyBehavior import FlyBehavior


class FlyWithWings(FlyBehavior):
    def fly(self) -> None:
        print("I'm flying!!")