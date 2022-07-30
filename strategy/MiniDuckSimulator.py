from DecoyDuck import DecoyDuck
from Duck import Duck
from FlyBehavior import FlyBehavior
from FlyNoWay import FlyNoWay
from FlyRocketPowered import FlyRocketPowered
from MallardDuck import MallardDuck
from ModelDuck import ModelDuck
from RubberDuck import RubberDuck
from Squeak import Squeak
from QuackBehavior import QuackBehavior


class MiniDuckSimulator:
    @staticmethod
    def main(*args):
        mallard: MallardDuck = MallardDuck()
        # canFly: FlyBehavior = lambda: print("I can't fly")
        # squeak: QuackBehavior = lambda: print("Squeak")
        canFly: FlyBehavior = FlyNoWay()
        squeak: QuackBehavior = Squeak()
        rubberDuckie: RubberDuck = RubberDuck(flyBehavior=canFly, quackBehavior=squeak)
        decoy: DecoyDuck = DecoyDuck()
        
        model: Duck = ModelDuck()
            
        mallard.performQuack()
        rubberDuckie.performQuack()
        decoy.performQuack()
        
        model.performFly()
        model.setFlyBehavior(FlyRocketPowered())
        model.performFly()

        
if __name__ == "__main__":
    MiniDuckSimulator.main()