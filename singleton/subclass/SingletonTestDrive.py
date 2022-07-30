from CoolerSingleton import CoolerSingleton
from HotterSingleton import HotterSingleton
from Singleton import Singleton


class SingletonTestDrive:
    @staticmethod
    def main(*args) -> None:
        foo: Singleton = CoolerSingleton.getInstance()
        bar: Singleton = HotterSingleton.getInstance()
        print(foo)
        print(bar)
        
if __name__ == "__main__":
    SingletonTestDrive.main()