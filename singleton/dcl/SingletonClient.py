from Singleton import Singleton


class SingletonClient:
    @staticmethod
    def main(*args) -> None:
        singleton: Singleton = Singleton.getInstance()
            
if __name__== "__main__":
    SingletonClient.main()