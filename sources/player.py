# Player class

class Player:
	#~ def __init__(self, major, gpa, items):
	def __init__(self, gpa, items=[]):

		#~ self.major = major
		self.gpa = gpa
		self.items = items

	def takeItem(self, item):

		self.items.append(item)
