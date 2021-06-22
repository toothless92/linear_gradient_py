# linear_gradient_py
Python module for finding the hex codes on a linear gradient, given an arbitrary number of colors and steps.

# Sample implementation:
~~~
from lingradpy import Linear_Gradient_Maker()

# Initialize object
lin_grad = Linear_Gradient_Maker()
\# Set number of steps from color to color
lin_grad.set_number_of_steps(input("Input number of steps from color to color: "))
# Add color points for the gradient
while True:
    color = input("Input next color code (######). Enter \'n\' to finish: ")
    if color == 'n':
        break
    lin_grad.add_color(color)
# Run the method to return the gradient code list
gradient = lin_grad.get_linear_gradient()
# Print results
print("\n")
for i in range(len(gradient[1:])+1):
    print(str(i) + ":\t" + gradient[i])
~~~
