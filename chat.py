def chat():
    import os 
    from problem import problem
    from restart import restart
    from messages import message1,message2,message3,message4,message5,message6

    os.system('color 3f')

    print(message1)
    userName = str(input(''))

    print('Ok',userName,message2)
    first = int(input(''))

    match first:
        case 1:
            print(message3)
        case 2:
            print(message4)
        case 3:
            print(message5)
        case 4:
            problem()
        case _: 
            print(message6)
            chat()
    restart()