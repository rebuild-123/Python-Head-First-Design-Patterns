import threading 

class Singleton:
    __uniqueInstance = None
    __lock__ = threading.Lock()
    
    def __init__(self):
        pass
    
    @staticmethod
    def getInstance():
        if Singleton.__uniqueInstance == None:
            with Singleton.__lock__:
                if Singleton.__uniqueInstance == None:
                    Singleton.__uniqueInstance = Singleton()
        return Singleton.__uniqueInstance
