from QuackBehavior import QuackBehavior


class MuteQuack(QuackBehavior):
    def quack(self) -> None:
        print("<< Silence >>")