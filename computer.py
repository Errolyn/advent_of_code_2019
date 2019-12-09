class Computer:
    def __init__(self, instruction, position = 0):
        options = {
            1 : self.add,
            2 : self.multiply,
            3 : self.get_input,
            4 : self.return_value,
            99: self.end_program
        }
        opcode = None
        arg1 = None
        arg2 = None

        self.instruction = instruction
        self.position = position
        self.options = options
        self.opcode = opcode
        self.arg1 = arg1
        self.arg2 = arg2

    # def get_optcode(self, instruction):



    def run_opcode(self, opcode):
        try:
            funct = self.options[opcode]
            return funct
        except KeyError:
            print(f"Invaid opcode: {opcode}")
        

    ## Instructions ##

    ## Command code 1: ##
    # Two behaviors default will use next two ints in instruction,
    # specific ints can be passed to function
    def add(self, x = None, y = None):  
        if x == None:
            x = self.instruction[self.position + 1]
        if y == None:
            y = self.instruction[self.position + 2]
        self.position += 3
        return x + y

    def multiply(self, x, y): #command code 2
        return x * y

    def get_input(self, *args): #command code 3
        while True:
            try:
                user_input = int(input("Input a number \n>>> "))
                return user_input
            except:
                print("Must be a number")

    def return_value(self, input_value, *args): #command code 4
        return input_value


    def end_program(self): #command code 99
        return "Exit"
