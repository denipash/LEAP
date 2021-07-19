#
# First Pythron Program: HelloWorld
#

def main():
    print("hello world!")
    name = input("What is your name? ")
    print("Nice to meet you,", name)

if __name__ == "__main__": #Checking when this file of Python is loaded, the interpreter will look to see if that value is equal to main
    main()

