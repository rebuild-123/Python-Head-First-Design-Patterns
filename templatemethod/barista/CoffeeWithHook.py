from CaffeineBeverageWithHook import CaffeineBeverageWithHook


class CoffeeWithHook(CaffeineBeverageWithHook):
    
    def brew(self) -> None:
        print("Dripping Coffee through filter")
        
    def addCondiments(self) -> None:
        print("Adding Sugar and Milk")
        
    def customerWantsCondiments(self) -> bool:
        answer: str = self.__getUserInput()
        if answer.lower().startswith('y'):
            return True
        else:
            return False
        
    def __getUserInput(self) -> str:
        answer = None
        print("Would you like milk and sugar with your coffee (y/n)? ")
        try:
            answer = input()
        except IOError:
            print("IO error trying to read your answer")
        if answer == None:
            return 'no'
        return answer