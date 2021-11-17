class simple:
    def sum(self, *args):
        if args[0][0] >= 0 and args[0][1] >= 0:
            print("sum: ", args[0][0]+args[0][1])
        else:
            print("NEGATIVE VALUES ARE NOT ACCEPTED")

    def sub(self, *args):
        if args[0][0] >= 0 and args[0][1] >= 0:
            print("difference: ", args[0][0]-args[0][1])
        else:
            print("NEGATIVE VALUE ARE NOT ACCCEPTED")

    def mul(self, *args):
        if args[0][0] >= 0 and args[0][1] >= 0:
            print("multiply: ", args[0][0]*args[0][1])
        else:
            print("NEGATIVE VALUE ARE NOT ACCCEPTED")

    def div(self, *args):
        if args[0][0] >= 0 and args[0][1] >= 0:
            print("divsion: ", (args[0][0])/(args[0][1]))
        else:
            print("NEGATIVE VALUE ARE NOT ACCCEPTED")


class complex_no(simple):
    def sum(self, *args):
        if len(args) == 4:
            if args[0] >= 0 and args[1] >= 0 and args[2] >= 0 and args[3] >= 0:
                r = args[0]+args[2]
                i = args[1]+args[3]
                print("sum: ", r, '+', i, 'j')
            else:
                print("NEGATIVE VALUE ARE NOT EXCEPTED")
        elif len(args) == 2:
            super().sum(args)

    def sub(self, *args):
        if len(args) == 4:
            if args[0] >= 0 and args[1] >= 0 and args[2] >= 0 and args[3] >= 0:
                r = args[0]-args[2]
                i = args[1]-args[3]
                if i >= 0:
                    print("difference: ", r, '+', i, 'j')
                else:
                    print("difference: ", r, i, 'j')
            else:
                print("NEGATIVE VALUE ARE NOT EXCEPTED")
        else:
            super().sub(args)

    def mul(self, *args):
        if len(args) == 4:
            if args[0] >= 0 and args[1] >= 0 and args[2] >= 0 and args[3] >= 0:
                r = args[0]*args[2] - args[1]*args[3]
                i = args[0]*args[3] + args[1]*args[2]
                if i >= 0:
                    print("multiply: ", r, "+", i, 'j')
                else:
                    print("multiply: ", r, i, 'j')
            else:
                print("NEGATIVE VALUE ARE NOT EXCEPTED")
        else:
            super().mul(args)

    def div(self, *args):
        try:
            if len(args) == 4:
                if args[0] >= 0 and args[1] >= 0 and args[2] >= 0 and args[3] >= 0:
                    r = (args[0]*args[2]+args[1]*args[3]) / \
                        (args[2]*args[2] + args[3]*args[3])
                    i = (args[1]*args[2]-args[0]*args[3]) / \
                        (args[2]*args[2] + args[3]*args[3])
                    if i >= 0:
                        print("division: ", r, '+', i, 'j')
                    else:
                        print("division: ", r, i, 'j')
                else:
                    print("NEGATIVE VALUE ARE NOT EXCEPTED")
            else:
                super().div(args)
        except:
            print("Can't divide by zero")


if __name__ == "__main__":

    print("***************CALCULATOR*****************")
    try:
        user = int(
            input("enter 1 for Simple Arithmetic\n2 for Complex Arithmetic\n"))
        if user == 1:
            n1 = float(input("Enter number1: "))
            n2 = float(input("Enter number2: "))
            operator = int(input(
                "enter 1 for addition\n enter 2 for subtraction\nenter 3 for multiplication\nenter 4 for division\n"))

            s1 = complex_no()
            if operator == 1:
                s1.sum(n1, n2)
            elif operator == 2:
                s1.sub(n1, n2)
            elif operator == 3:
                s1.mul(n1, n2)
            elif operator == 4:
                s1.div(n1, n2)
            else:
                print("INVALID OPERATOR")
        elif user == 2:
            n1 = float(input("Enter real part of number1: "))
            n2 = float(input("Enter imaginary part of number2: "))
            n3 = float(input("Enter real part of number1: "))
            n4 = float(input("Enter imaginary part of number2: "))
            operator = int(input(
                "enter 1 for addition\n enter 2 for subtraction\nenter 3 for multiplication\nenter 4 for division\n"))

            s2 = complex_no()
            if operator == 1:
                s2.sum(n1, n2, n3, n4)
            elif operator == 2:
                s2.sub(n1, n2, n3, n4)
            elif operator == 3:
                s2.mul(n1, n2, n3, n4)
            elif operator == 4:
                s2.div(n1, n2, n3, n4)
            else:
                print("INVALID OPERATOR")
        else:
            print("choose between 1 or 2")

    except:
        print("enter a correct value Invalid Option")
