
# class real:
#     def __init__(self, *args):
#         self.args = args

# class real:
#     def caculation_type(*args):
#         if (len(args) == 2):
#             # args[0], args[1] = int(input("enter two real number\n").split())
#             print(args[0]+args[1])


# s1 = real()
# s1.caculation_type(3, 5)
#
# ****************************************************************

# SOME SUCCESS

# class real:
#     def sum(self, *args):
#         if (len(args) == 2):
#             print("sum of numbers:", args[0]+args[1])
#         else:
#             print("sum of numbers:", args[0] +
#                   args[2], "+", args[1]+args[3], "j")


# s1 = real()
# s1.sum(2, 4)
# s1.sum(2, 4, 4, 5)
# *********************************************************************
# ***********************************************************

# class real:
#     def sum(self, *args):
#         print(args[0]+args[1])


# class complex(real):
#     def sum(self, *args):
#         if len(args) == 4:
#             r = args[0]+args[2]
#             i = args[1]+args[3]
#             print(r, "+", i, "j")
#         elif(len(args) == 2):
#             return super().sum()


# s1 = complex()
# s1.sum(3, 6)
# s1.sum(3, 6, 4, 5)
# ********************************************************
# NOT WORKING
# class real:

#     def sum(self, *args):
#         print("sum:", args[0]+args[1])


# class complex(real):
#     def sum(self, *args):
#         if len(args) == 4:
#             r = args[0]+args[2]
#             i = args[1]+args[3]
#             print(r, "+", i, "j")
#         else:
#             return super().sum()


# s1 = complex()
# s1.sum(3, 4, 5, 8)
# s1.sum(3, 5)
# **************************************************************

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
