from Quackable import Quackable


class DecoyDuck(Quackable):
    def quack(self) -> None:
        print("<< Silence >>")