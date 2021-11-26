
def enter_age():
    age = input('Enter your Age : ')
    print(type(age))
    try : 
        age = int(age)
    except ValueError:
        age = 0
        
    print(age)
    print(type(age))
