from SimpleObserver import SimpleObserver
from SimpleSubject import SimpleSubject


class Example:
    @staticmethod
    def main(*args):
        simpleSubject: SimpleSubject = SimpleSubject()
        simpleObserver: SimpleObserver = SimpleObserver(simpleSubject)
        simpleSubject.setValue(80)
        simpleSubject.removeObserver(simpleObserver)
        
        
if __name__ == "__main__":
    Example.main()