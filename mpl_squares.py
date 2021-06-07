import matplotlib.pyplot as plt 

input_values = [1, 2, 3, 4, 5]

squares = [1, 4, 9, 16, 26]
plt.plot(input_values, squares, linewidth = 5)

#Defining title and labels
plt.title("Numbers squares", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("squares value")

#Defining size of labels
plt.tick_params(axis="both", labelsize = 14)

plt.show()