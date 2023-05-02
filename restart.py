def restart():
    from problem import problem
    from chat import chat
    from messages import message7,message2_1,message3,message4,message5,message6
    print(message7)
    continuee = str(input())
    continuee = continuee.lower()
    while continuee == "r":
        print(message2_1)
        second = int(input(''))
        match second:
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