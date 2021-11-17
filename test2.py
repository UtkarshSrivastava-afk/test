class simple:

    def sum(self, *args):
        print(args[0][0]+args[0][1])


class complex_no(simple):

    def sum(self, *args):
        if len(args) == 4:
            r = args[0]+args[2]
            i = args[1]+args[3]
            print("sum: ", r, '+', i, 'j')
        elif len(args) == 2:
            super().sum(args)


s1 = complex_no()
s1.sum(3, 4, 6, 8)
s1.sum(3, 8)
