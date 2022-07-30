from enum import auto, Enum


class Singleton(Enum):
    UNIQUE_INSTANCE = auto()
    
    def getDescription(self) -> str:
        return "I'm a thread safe Singleton!"