class Singleton:
    __uniqueInstance = None
    
    def __init__(self):
        pass
    
    @staticmethod
    def getInstance():
        if Singleton.__uniqueInstance == None:
            Singleton.__uniqueInstance = Singleton()
        return Singleton.__uniqueInstance
    
    # other useful methods here
    def getDescription(self) -> str:
        return "I'm a classic Singleton!"