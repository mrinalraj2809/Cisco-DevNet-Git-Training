def printNames(name, collegeName):
    for i in range(5):
        print(name + " " + collegeName)

if __name__ == '__main__':
    name = ""+input("Enter your name: ")
    college = ""+input("Enter your college name: ")
    printNames(name,college)
