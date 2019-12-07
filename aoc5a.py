# compute = [1,9,10,3,2,3,11,0,99,30,40,50]

# compute = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,10,19,23,2,9,23,27,1,6,27,31,1,10,31,35,1,35,10,39,1,9,39,43,1,6,43,47,1,10,47,51,1,6,51,55,2,13,55,59,1,6,59,63,1,10,63,67,2,67,9,71,1,71,5,75,1,13,75,79,2,79,13,83,1,83,9,87,2,10,87,91,2,91,6,95,2,13,95,99,1,10,99,103,2,9,103,107,1,107,5,111,2,9,111,115,1,5,115,119,1,9,119,123,2,123,6,127,1,5,127,131,1,10,131,135,1,135,6,139,1,139,5,143,1,143,9,147,1,5,147,151,1,151,13,155,1,5,155,159,1,2,159,163,1,163,6,0,99,2,0,14,0]
# i = 0

# def command_handler(command, x, y):
#     if command == 1:
#         return x + y
#     elif command == 2:
#         return x * y
    

# while i < (len(compute)):
#     command = compute[i]
#     i += 1
#     x = compute[i]
#     i += 1
#     y = compute[i]
#     i += 1
#     compute[compute[i]] = command_handler(command, compute[x], compute[y])
#     i += 1
#     if compute[i] == 99:
#         break

# print(compute[0])

## Program Fetcher ##
def get_program():
    try:
        usable_program = compute
    except NameError:
        usable_program = list(map(int, input("Enter your program \n >>> ").split(",")))
    return usable_program

## Main program functions ##
def op_code_handler( opcode, first_arg, second_arg, mode = (0,0,0) ):
    if opcode == 1:
        return first_arg + second_arg
    elif opcode == 2:
        return first_arg * second_arg    

def program_runner(code, location, program):
    if code == 99:
        return "Done"

    if len(str(code)) == 1:
        arg1 = program[location + 1]
        arg2 = program[location + 2]
        output_loc = program[location + 3]
        program[output_loc] = op_code_handler(code, (program[arg1]), (program[arg2]))
        return(4)
    elif len(str(code)) > 1:
        print(NotImplemented)

def main():
    compute = get_program()
    program_location = 0
    program = compute.copy()
    while program_location < len(program):
        code = program[program_location]
        program_response = program_runner(code, program_location, program)
        if program_response == "Done":
            break
        else:
            program_location += program_response
    print(f"Your output is: {program[0]}")

if __name__ == "__main__":
    main()