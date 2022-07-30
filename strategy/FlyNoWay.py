from abc import ABC, abstractmethod

from FlyBehavior import FlyBehavior


class FlyNoWay(FlyBehavior):
    def fly(self) -> None:
        print("I can't fly")