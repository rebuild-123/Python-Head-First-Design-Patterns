from LG import LG
from Sony import Sony
from TV import TV


class TVFactory:
    def getTV(self, type_: str) -> TV:
        if type_ == 'LG':
            return LG()
        elif type_ == 'Sony':
            return Sony()
        else:
            raise Exception("Invalid TV Type")