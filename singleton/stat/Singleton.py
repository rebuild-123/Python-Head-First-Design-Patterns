class Singleton:
    # __uniqueInstance = Singleton() # python can not do this.
    
    __uniqueInstance = None
    
    def __new__(cls):
        if not cls.__uniqueInstance:
            Singleton.__uniqueInstance = super().__new__(cls)
        return cls.__uniqueInstance
    
    def __init__(self):
        pass
    
    # # it can not work.
    # @staticmethod
    # def getInstance():
    #     return Singleton.__uniqueInstance
    
    def getInstance(self):
        return self.__uniqueInstance
    
    # other useful methods here
    def getDescription(self) -> str:
        return "I'm a statically initialized Singleton!"