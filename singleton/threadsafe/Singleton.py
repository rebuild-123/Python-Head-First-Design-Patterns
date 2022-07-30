import threading 


class Singleton:
    __uniqueInstance = None
    __lock__ = threading.Lock()
    
    # other useful instance variables here
    
    def __init__(self):
        pass
    
    @staticmethod
    def getInstance():
        with Singleton.__lock__:
            if Singleton.__uniqueInstance == None:
                Singleton.__uniqueInstance = Singleton()
            return Singleton.__uniqueInstance
        
    # other useful methods here
    def getDescription(self) -> str:
        return "I'm a thread safe Singleton!"