# Day 2 Part A

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


# Day 2 Part B

compute_data = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,10,19,23,2,9,23,27,1,6,27,31,1,10,31,35,1,35,10,39,1,9,39,43,1,6,43,47,1,10,47,51,1,6,51,55,2,13,55,59,1,6,59,63,1,10,63,67,2,67,9,71,1,71,5,75,1,13,75,79,2,79,13,83,1,83,9,87,2,10,87,91,2,91,6,95,2,13,95,99,1,10,99,103,2,9,103,107,1,107,5,111,2,9,111,115,1,5,115,119,1,9,119,123,2,123,6,127,1,5,127,131,1,10,131,135,1,135,6,139,1,139,5,143,1,143,9,147,1,5,147,151,1,151,13,155,1,5,155,159,1,2,159,163,1,163,6,0,99,2,0,14,0]
stop_at = len(compute_data) - 1

def command_handler(command, x, y):
    if command == 1:
        return(int(x + y))
    elif command == 2:
        return(int(x * y))
    else:
        print(f"I received a bad command: {command}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def computer(compute):
    
    i = 0
    while i < stop_at:
        
        if compute[i] == 99:
            break
        command = compute[i]
        i += 1
        x = compute[i]
        i += 1
        y = compute[i]
        i += 1
        compute[compute[i]] = command_handler(command, compute[x], compute[y])

        if compute[0] == 19690720:
            print(100*compute[1]+compute[2])
            break

        i += 1

for noun in range(100):
    for verb in range(100):
        compute = compute_data.copy()
        compute[1] = noun
        compute[2] = verb
        computer(compute)


print(compute[0])



