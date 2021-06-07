from random import choice

class RandomWalk(object):
	"""Class designed to generating Random Walk."""

	def __init__(self, num_points=5000):
		super(RandomWalk, self).__init__()
		self.num_points = num_points

		#Starting position
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		"""Generating all random points for random walk"""
		
		#Doing steps until achieving expected point number
		while len(self.x_values) < self.num_points:
			#Setting direction and distance to beat in this direction
			x_step = get_step()
			y_step = get_step()

			#Discarding moves that leads nowhere
			if x_step == 0 and y_step == 0:
				continue

			#Calculating next values of X and Y
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			self.x_values.append(next_x)
			self.y_values.append(next_y)

def get_step():
	#Setting direction and distance to beat in this direction
	direction = choice([1, -1])
	distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
	sumdd = direction * distance
	return sumdd