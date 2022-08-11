from GenericRemote import GenericRemote
from SpecialRemote import SpecialRemote
from TVFactory import TVFactory


class Client:
    @staticmethod
    def main(*args) -> None:
        tvFactory: TVFactory = TVFactory()
        remoteSony: SpecialRemote = SpecialRemote(tvFactory)
        print("Connect your remote to the TV")
        remoteSony.setTV("Sony")
        remoteSony.on()
        remoteSony.up()
        remoteSony.down()
        remoteSony.off()
        
        remoteLG: GenericRemote = GenericRemote(tvFactory)
        print("Connect your remote to the TV")
        remoteLG.setTV("LG")
        remoteLG.on()
        remoteLG.nextChannel()
        remoteLG.prevChannel()
        remoteLG.off()
        
if __name__ == "__main__":
    Client.main()