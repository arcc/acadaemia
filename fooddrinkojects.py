from objects import gameObject

class FoodDrink(gameObject):

  def __init__(self, **kwargs):
    super(FoodDrink, self).__init__(**kwargs)
    self.effect = {}

class apple(FoodDrink):
    def __init__(self, effect, weight, value):
        super(apple, self).__init__(weight = weight, value = value)
        self.effect = effect


class banana(FoodDrink):
    def __init__(self, effect, weight, value):
        super(banana, self).__init__(weight = weight, value = value)
        self.effect = effect

    def store(self):
        pass
class chocolate(FoodDrink):
    def __init__(self, effect, weight, value):
        super(chocolate, self).__init__(weight = weight, value = value)
        self.effect = effect

class beer(FoodDrink):
    def __init__(self, effect, weight, value):
        super(beer, self).__init__(weight = weight, value = value)
        self.effect = effect

class water(FoodDrink):
    def __init__(self, effect, weight, value):
        super(water, self).__init__(weight = weight, value = value)
        self.effect = effect

class sandwich(FoodDrink):
    def __init__(self, effect, weight, value):
        super(sandwich, self).__init__(weight = weight, value = value)
        self.effect = effect

class pasta(FoodDrink):
    def __init__(self, effect, weight, value):
        super(pasta, self).__init__(weight = weight, value = value)
        self.effect = effect

class eggs(FoodDrink):
    def __init__(self, effect, weight, value):
        super(eggs, self).__init__(weight = weight, value = value)
        self.effect = effect
