import matplotlib.pyplot as plt 

from random_walk import RandomWalk

#Creating new Random walk as long as program is active
while True:
	#Preparing random walking data and displaying points
	rw = RandomWalk(50000)
	rw.fill_walk()

	#Setting the size of the plot window
	plt.figure(figsize = (10,6))

	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values , c = point_numbers,
		cmap = plt.cm.Blues, edgecolor = "none", s = 1)

	#highlighting first and last point of random walk
	plt.scatter(0, 0, c = "green", edgecolors = "none", s = 100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c = "red",
	 edgecolors = "none", s = 100)

	#hiding axis
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()

	keep_running = input("Create a new RandomWalk? (y/n):")
	if keep_running == "n":
		break
