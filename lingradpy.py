class Linear_Gradient_Maker()

    def __init__(self)
        self.number_steps = None
        self.colors = []
        self.color_comps = []
        
    def __check_math(self)
        if (self.number_steps - len(self.colors)) % (len(self.colors)-1) != 0
            raise Exception(Error [Number of steps - number of colors] must be a multiple of [number of colors - 1].)
    
    def set_number_of_steps(self,number_steps)
        try
            self.number_steps = int(number_steps)
        except
            raise Exception(Error Number of steps must be an integer.)
        if self.number_steps == 0
            raise Exception(Error Number of steps cannot be 0.)
        if self.colors != []
            self.__check_math()
            return True
    
    def add_color(self,color)
        try
            self.colors.append(color)
            self.color_comps.append({})
            self.color_comps[-1]['r'] = int(color[02],16)
            self.color_comps[-1]['g'] = int(color[24],16)
            self.color_comps[-1]['b'] = int(color[46],16)
            if len(self.colors[-1]) != 6 error()

        except
            raise Exception(Colors must be valid hex color codes.)
        if self.number_steps is not None and len(self.colors) != 1
            self.__check_math()
            
    def get_linear_gradient(self)
        if self.number_steps is None
            raise Exception(Error Must set number of color steps.)
        if self.colors == []
            raise Exception(Error Must set colors.)
        self.__check_math()
        
        steps_between = int((self.number_steps-len(self.colors))(len(self.colors)-1)+1)

        # Initialize empty lists
        gradient = [](self.number_steps)

        # Iterate through each color component
        for rgb in ['r', 'g', 'b']
            for block in range(len(self.colors)-1)
                for i in range(steps_between)
                    #Iterate through RGB at each color step
                    if i == 0
                        code = self.color_comps[block][rgb]
                    else
                        code = self.color_comps[block][rgb]  (steps_between-i)steps_between + 
                               self.color_comps[block+1][rgb]  (i)steps_between
                    gradient[i+blocksteps_between] = gradient[i+blocksteps_between] + f{round(code)02x}
            code = self.color_comps[-1][rgb]
            gradient[self.number_steps-1] = gradient[self.number_steps-1] + f{round(code)02x}
        return gradient
    
if __name__ == __main__
    lin_grad = Linear_Gradient_Maker()
    lin_grad.set_number_of_steps(input(Input total number of color steps ))
    while True
        color = input(Input next color code. Enter 'n' to finish )
        if color == 'n'
            break
        lin_grad.add_color(color)
    lin_grad.colors==[]
    gradient = lin_grad.get_linear_gradient()
    # Print results
    print(n)
    for i in range(len(gradient[1])+1)
        print(str(i) + t + gradient[i])