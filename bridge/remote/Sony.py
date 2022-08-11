from TV import TV


class Sony(TV):
    station: int = 0
    def on(self) -> None:
        print("Turning on the Sony TV")
    def off(self) -> None:
        print("Turning off the Sony TV");
    def tuneChannel(self, channel: int) -> None:
        self.station = channel
        print(f"Set the Sony TV station to {self.station}")
    def getChannel(self) -> int:
        return self.station