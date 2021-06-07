import matplotlib.pyplot as plt 

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues,
 edgecolor = "none", s = 40)

#Defining title and labels
plt.title("Numbers squares", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("squares value")

#Defining size of labels
plt.tick_params(axis = "both", which = "major", labelsize = 14)

#Defining the range for each axis
plt.axis([0, 1100, 0, 1100000])

plt.savefig("squares_plot.png", bbox_inches = "tight")