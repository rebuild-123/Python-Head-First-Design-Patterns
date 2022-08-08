from Menu import Menu
from MenuComponent import MenuComponent
from MenuItem import MenuItem
from Waitress import Waitress


class MenuTestDrive:
    @staticmethod
    def main(*args):
        pancakeHouseMenu: MenuComponent = Menu("PANCAKE HOUSE MENU", "Breakfast")
        dinerMenu: MenuComponent = Menu("DINER MENU", "Lunch")
        cafeMenu: MenuComponent = Menu("CAFE MENU", "Dinner")
        dessertMenu: MenuComponent = Menu("DESSERT MENU", "Dessert of course!")
        coffeeMenu: MenuComponent = Menu("COFFEE MENU", "Stuff to go with your afternoon coffee")
            
        allMenus: MenuComponent = Menu("ALL MENUS", "All menus combined")
            
        allMenus.add(pancakeHouseMenu)
        allMenus.add(dinerMenu)
        allMenus.add(cafeMenu)
        
        pancakeHouseMenu.add(MenuItem( "K&B's Pancake Breakfast", "Pancakes with scrambled eggs and toast", True, 2.99))
        pancakeHouseMenu.add(MenuItem( "Regular Pancake Breakfast", "Pancakes with fried eggs, sausage", False, 2.99))
        pancakeHouseMenu.add(MenuItem( "Blueberry Pancakes", "Pancakes made with fresh blueberries and blueberry syrup", True, 3.49))
        pancakeHouseMenu.add(MenuItem( "Waffles", "Waffles with your choice of blueberries or strawberries", True, 3.59))
        
        dinerMenu.add(MenuItem( "Vegetarian BLT", "(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99))
        dinerMenu.add(MenuItem( "BLT", "Bacon with lettuce & tomato on whole wheat", False, 2.99))
        dinerMenu.add(MenuItem( "Soup of the day", "A bowl of the soup of the day, with a side of potato salad", False, 3.29))
        dinerMenu.add(MenuItem( "Hot Dog", "A hot dog, with saurkraut, relish, onions, topped with cheese", False, 3.05))
        dinerMenu.add(MenuItem( "Steamed Veggies and Brown Rice", "A medly of steamed vegetables over brown rice", True, 3.99))
        dinerMenu.add(MenuItem( "Pasta", "Spaghetti with marinara sauce, and a slice of sourdough bread", True, 3.89))
        dinerMenu.add(dessertMenu)
        
        dessertMenu.add(MenuItem( "Apple Pie", "Apple pie with a flakey crust, topped with vanilla icecream", True, 1.59))
        dessertMenu.add(MenuItem( "Cheesecake", "Creamy New York cheesecake, with a chocolate graham crust", True, 1.99))
        dessertMenu.add(MenuItem( "Sorbet", "A scoop of raspberry and a scoop of lime", True, 1.89))
        
        cafeMenu.add(MenuItem( "Veggie Burger and Air Fries", "Veggie burger on a whole wheat bun, lettuce, tomato, and fries", True, 3.99))
        cafeMenu.add(MenuItem( "Soup of the day", "A cup of the soup of the day, with a side salad", False, 3.69))
        cafeMenu.add(MenuItem( "Burrito", "A large burrito, with whole pinto beans, salsa, guacamole", True, 4.29))
        
        cafeMenu.add(coffeeMenu)
        
        coffeeMenu.add(MenuItem("Coffee Cake", "Crumbly cake topped with cinnamon and walnuts", True, 1.59))
        coffeeMenu.add(MenuItem("Bagel", "Flavors include sesame, poppyseed, cinnamon raisin, pumpkin", False, 0.69))
        coffeeMenu.add(MenuItem("Biscotti", "Three almond or hazelnut biscotti cookies", True, 0.89))
        
        waitress: Waitress = Waitress(allMenus)
            
        waitress.printMenu() # book's example
        
if __name__ == "__main__":
    MenuTestDrive.main()