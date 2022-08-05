from abc import ABC, abstractmethod

from ShareStrategy import ShareStrategy


class PhoneCameraApp(ABC):
    shareStrategy: ShareStrategy
        
    def setShareStrategy(self, shareStrategy: ShareStrategy) -> None:
        self.shareStrategy = shareStrategy
        
    def share(self) -> None:
        self.shareStrategy.share()
        
    def take(self) -> None:
        print("Taking the photo")
        
    def save(self) -> None:
        print("Saving the photo")
        
    @abstractmethod
    def edit(self) -> None:
        pass