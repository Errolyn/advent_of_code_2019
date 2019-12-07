class Computer:

    ## REMOVE ##
    opcode = 1
    arg1 = 2
    arg2 = 3

    def __init__(self, instruction, position):
        options = {
            1 : self.add,
            2 : self.multiply,
            3 : self.get_input,
            99: self.end_program
        }
        self.instruction = instruction
        self.position = position
        self.options = options

    def run_opcode(self, opcode):
        try:
            funct = self.options[opcode]()
            return funct
        except KeyError:
            print(f"Invaid opcode: {opcode}")
        

    ## Instructions ##
    def add(self, x = arg1, y = arg2): #command code 1
        return x + y

    def multiply(self, x = arg1, y = arg2): #command code 2
        return x * y

    def get_input(self): #command code 3
        while True:
            try:
                user_input = int(input("Input a number \n>>> "))
                return user_input
            except:
                print("Must be a number")

    def end_program(self):
        return "Exit"
