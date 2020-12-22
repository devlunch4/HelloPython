def showdan (dan):
    print(str(dan) + " * 1 = " + str(dan * 1))
    print(str(dan) + " * 2 = " + str(dan * 2))
    print(str(dan) + " * 3 = " + str(dan * 3))
    
    print(str(dan) + " * 4 = " + str(dan * 4))
    print(str(dan) + " * 5 = " + str(dan * 5))
    print(str(dan) + " * 6 = " + str(dan * 6))
    
    print(str(dan) + " * 7 = " + str(dan * 7))
    print(str(dan) + " * 8 = " + str(dan * 8))
    print(str(dan) + " * 9 = " + str(dan * 9))


def showdan1 (a):
    for i in range(9):
        print(str(a) + " * " + str(i + 1) + " = " + str(a * (i + 1)))

showdan(3)
print()
showdan1(4)
