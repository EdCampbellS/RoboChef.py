class RoboChef:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def cook(self):
        if len(self.ingredients) == 0:
            print("No ingredients found. Please add ingredients before cooking.")
            return

        print("Cooking delicious meal with the following ingredients:")
        for ingredient in self.ingredients:
            print("- " + ingredient)

        print("Enjoy your meal!")

def main():
    chef = RoboChef()

    # Add ingredients to the RoboChef's list
    chef.add_ingredient("Tomato")
    chef.add_ingredient("Onion")
    chef.add_ingredient("Garlic")
    chef.add_ingredient("Salt")
    chef.add_ingredient("Pepper")

    # Cook the meal
    chef.cook()

if __name__ == "__main__":
    main()
