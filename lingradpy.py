class Linear_Gradient_Maker():

    '''
    This module is for calculating the hex color codes of a gradient going through
    an arbitrary number of colors.  The result is a linear gradient between each
    ajacent color.
    
    Written by Mike Reilly. Please contact mreilly92@gmail.com with questions.
    '''

    def __init__(self):
    # Set empty things
        self.steps_between = None
        self.colors = []
        self.color_comps = []
    
    def set_number_of_steps(self,steps_between):
        # Use this method to set the number of steps from color to color.
        # E.g. a value of '10' with two colors will give 11 total points.
        #      a value of '10' with three colors will give 21 total points. 
        try:
            # Fix data types
            self.steps_between = int(steps_between)
        except:
            # Handler for non-numbers being entered
            raise Exception("Error: Number of steps must be an integer.")
        if self.steps_between == 0:
            # Can't have zero steps
            raise Exception("Error: Number of steps cannot be 0.")
    
    def add_color(self,color):
        # Use this method to add more color points (one with each call)
        # to draw gradients between.
        try:
            # Add new color code to list
            self.colors.append(color)
            # Test to make sure the value given is 6 characters long
            if len(self.colors[-1]) != 6: error()
            # Red, green, and blue values are stored separately.
            self.color_comps.append({})
            self.color_comps[-1]['r'] = int(color[0:2],16)
            self.color_comps[-1]['g'] = int(color[2:4],16)
            self.color_comps[-1]['b'] = int(color[4:6],16)
        except:
            # Catch errors from converting hex to int, which will
            # indicate that the user used an incorrect format.
            raise Exception("Colors must be valid hex color codes in format ######.")
            
    def get_linear_gradient(self):
        # This method returns the list of color codes for the full gradient
        if self.steps_between is None:
            raise Exception("Error: Must set number of color steps.")
        if self.colors == []:
            raise Exception("Error: Must set colors.")

        # Initialize empty lists
        gradient = [""]*(self.number_steps)
        
        for rgb in ['r', 'g', 'b']:
        # Iterate through each color component
            for block in range(len(self.colors)-1):
            # Iterate through each gradient segment
                for i in range(steps_between):
                    # Iterate through each step in the gradient segment
                    if i == 0:
                        # The first step, which is one of the anchor colors
                        code = self.color_comps[block][rgb]
                    else:
                        # Calculate the new RGB values using a linear weighting calculation
                        code = self.color_comps[block][rgb] * (steps_between-i)/steps_between + \
                               self.color_comps[block+1][rgb] * (i)/steps_between
                     # Append the list element with the hex code. Integers are rounded before conversion.
                    gradient[i+block*steps_between] = gradient[i+block*steps_between] + f"{round(code):02x}"
            # Do last color value
            code = self.color_comps[-1][rgb]
            number_steps = (len(self.colors)-1)*self.steps_between + 1
            gradient[self.number_steps-1] = gradient[self.number_steps-1] + f"{round(code):02x}"
        # Return list of RGB hex code strings
        return gradient
    
if __name__ == "__main__":
    # Sample implementation:
    # Initialize object
    lin_grad = Linear_Gradient_Maker()
    # Set number of steps from color to color
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