katz_deli = []

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    elif len(katz_deli) >= 1:
        num = 1
        listing = ''
        for name in katz_deli:
            listing += (f' {num}. {name}')
            num += 1
        print(f'The line is currently:{listing}')

def take_a_number(katz_deli, name):
    new_number = len(katz_deli) + 1
    katz_deli.append(name)
    print(f'Welcome, {name}. You are number {new_number} in line.')
    
def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        name = katz_deli[0]
        print(f'Currently serving {name}.')
        katz_deli.pop(0)