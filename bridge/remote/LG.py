from TV import TV


class LG(TV):
    channel: int = 1
    def on(self) -> None:
        print("Turning on the LG TV")
    def off(self) -> None:
        print("Turning off the LG TV")
    def tuneChannel(self, channel: int) -> None:
        self.channel = channel
        print(f"Set the LG TV Channel to {self.channel}")
    def getChannel(self) -> int:
        return self.channel