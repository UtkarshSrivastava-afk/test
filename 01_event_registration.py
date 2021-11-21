class participant:
    def __init__(self, name, rollno, branch, gender):
        self.name = name
        self.rollno = rollno
        self.branch = branch
        self.gender = gender

    def registration(self):
        print("****** REGISTRATION PROCESS STARTED")
        print("          ****YOUR DETAILS****")
        print(f" your name : {self.name}\nyour rollno : {self.rollno}")
        print(
            f" your branch : {self.branch}\nyour gender : {self.gender} ")


n = input("enter your name\n")
r = int(input("enter your rollno\n"))
b = input("enter your branch\n")
g = input("enter your gender\n")
a1 = participant(n, r, b, g)
a1.registration()
signal = input('''****TO CONTINUE ENTER "YES" FOR TERMINATION ENTER "NO"\n''')
if signal == "YES":
    with open('eventres.txt', 'a') as f:
        f.writelines(f"your name : {n}\n your rollno : {r}\n")
        f.writelines(f"your branch : {b}\n your gender : {g}\n")
    print("REGISTRATION SUCCESSFUL :-)")
else:
    print("REGISTRATION FAILED :/")
