import random

def oneSpinChara():
    result = random.randint(1, 100)

    match result:
        case n if n <= 5:
            print('5%')
        case n if n <= 20 and n > 5:
            print("15%")
        case n if n <= 100 and n > 20:
            print("80%")



def tenSpinChara():
    tempSpin = []
    i = 1

    while i <= 10:
        result = random.randint(1, 100)
        if i == 10 and 15 not in tempSpin:
            print('15%')
            break
        match result:
            case n if n <= 5:
                tempSpin.append(5)
                print('5%')
            case n if n <= 20 and n > 5:
                tempSpin.append(15)
                print("15%")
            case n if n <= 100 and n > 20:
                tempSpin.append(80)
                print("80%")
        i += 1

tenSpinChara()