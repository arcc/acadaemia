from objects import gameObject


class FoodDrink(gameObject):

  def __init__(self, **kwargs):
    super(FoodDrink, self).__init__(**kwargs)
    self.effect = {}


class Paper(gameObject):

  def __init__(self, length):
    self.message = ""
    self.weight = 0


# class WritingUtensils
