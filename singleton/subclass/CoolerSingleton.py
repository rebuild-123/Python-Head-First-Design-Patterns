from Singleton import Singleton


class CoolerSingleton(Singleton):
    # useful instance variables here
    __uniqueInstance = None
    
    def __init__(self):
        super().__init__()
        
    # useful methods here