from CaffeineBeverageWithHook import CaffeineBeverageWithHook


class TeaWithHook(CaffeineBeverageWithHook):
    
    def brew(self) -> None:
        print("Steeping the tea")
        
    def addCondiments(self) -> None:
        print("Adding Lemon")
        
    def customerWantsCondiments(self) -> bool:
        answer: str = self.__getUserInput()
        
        if answer.lower().startswith('y'):
            return True
        else:
            return False
        
    def __getUserInput(self) -> str:
        answer: str = None
        print("Would you like lemon with your tea (y/n)? ")
        try:
            answer = input()
        except IOError:
            print("IO error trying to read your answer")
        if answer == None:
            return "no"
        return answer