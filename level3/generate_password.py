import random
def create_password():

    while(True):
        try:
            long = (input("write long pass = "))
            long =int(long)
            break
        except ValueError:
            print('it is not number')
            continue


    password =''

    for i in range(long):
        choice  = random.randrange(1,5)
        if choice == 1:
            password+=chr(random.randrange(48,58))
        elif choice == 2:
            password+= chr(random.randrange(65,91))
        elif choice ==3:
            password+= chr(random.randrange(97,123))
        elif choice == 4:
            password+= random.choice('!*_%()?@')
    return  password


def create_list_password():
    pass_list =[]

    for i in range(4):
        pass_list.append(create_password())

    set_password = set(pass_list)
    long =len(set_password)
    while long < 4:
        pass_list.append(create_password())
        set_password = set(pass_list)
        long = len(set_password)

    print(pass_list)
    print(set_password)

    return set_password



create_list_password()








