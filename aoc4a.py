import re

start = 372037
end = 905157

valid_passwords = []

def check_for_rules(current_number):
    last = 0
    is_acending = True
    has_dubbles = False
    stringy_num = str(current_number)
    for i in stringy_num:
        if last > int(i):
            is_acending = False
        if last == int(i):
            if len(re.findall(i, stringy_num)) == 2:
                has_dubbles = True
        last = int(i)
    return(is_acending + has_dubbles)


for number in range(start, end):
    is_valid_password = check_for_rules(number)
    
    if is_valid_password == 2:
        print(f"Appended {number}")
        valid_passwords.append(number)

print(len(valid_passwords))