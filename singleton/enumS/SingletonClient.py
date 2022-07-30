from Singleton import Singleton


class SingletonClient:
    @staticmethod
    def main(*args) -> None:
        singleton: Singleton = Singleton.UNIQUE_INSTANCE
        print(singleton.getDescription())
        
if __name__ == "__main__":
    SingletonClient.main()