class calculate:
    def add(self, *args):
        if len(args) == 4:
            r = args[0]+args[2]
            i = args[1]+args[3]
            print('sum: ', r, "+", i, "j")
        else:
            print("sum:", args[0]+args[1])

    def sub(self, *args):
        if len(args) == 4:
            r = args[0]-args[2]
            i = args[1]-args[3]
            if i > 0:
                print("difference: ", r, '+', i, 'j')
            else:
                print("difference: ", r, i, 'j')

        else:
            print("difference: ", args[0]-args[1])

    def mul(self, *args):
        if len(args) == 4:
            r = args[0]*args[2] - args[1]*args[3]
            i = args[0]*args[3] + args[1]*args[2]
            if i > 0:
                print("multiply: ", r, "+", i, 'j')
            else:
                print("multiply: ", r, i, 'j')
        else:
            print("multiply: ", args[0]*args[1])

    def div(self, *args):
        try:
            if len(args) == 4:

                r = (args[0]*args[2]+args[1]*args[3]) / \
                    (args[2]*args[2] + args[3]*args[3])
                i = (args[1]*args[2]-args[0]*args[3]) / \
                    (args[2]*args[2] + args[3]*args[3])
                if i > 0:
                    print("division: ", r, '+', i, 'j')
                else:
                    print("division: ", r, i, 'j')
            else:
                print('division: ', args[0]/args[1])
        except:
            print("Can't divide by zero")


s1 = calculate()
s1.add(2, 3, 4, 5)
s1.sub(2, 3, 4, 5)
s1.sub(2, 8, 4, 5)
s1.mul(2, 8, 4, 5)
s1.div(2, 8, 4, 5)
s1.add(2, 5)
s1.sub(2, 5)
s1.mul(2, 5)
s1.div(2, 5)
