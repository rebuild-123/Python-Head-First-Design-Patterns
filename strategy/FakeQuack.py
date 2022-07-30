from QuackBehavior import QuackBehavior


class FakeQuack(QuackBehavior):
    def quack(self) -> None:
        print("Qwak")