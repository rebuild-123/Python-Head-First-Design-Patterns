from Duck import Duck
from FlyRocketPowered import FlyRocketPowered
from MallardDuck import MallardDuck
from ModelDuck import ModelDuck


class MiniDuckSimulator:
    @staticmethod
    def main(*args):
        mallard: MallardDuck = MallardDuck()
        mallard.performQuack()
        mallard.performFly()
        
        model: Duck = ModelDuck()
        model.performFly()
        model.setFlyBehavior(FlyRocketPowered())
        model.performFly()

        
if __name__ == "__main__":
    MiniDuckSimulator.main()