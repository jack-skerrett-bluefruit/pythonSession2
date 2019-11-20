import sys


def fib(n):
    a, b = 0, 1   
    for i in range(n):
        a, b = b, a+b
    return a



def Main():  
    answer = fib(int(sys.argv[1]))
    print("The " + str(sys.argv[1]) +"th " + "number in the Fibonacci sequence is " + str(answer))






def imported():
    print("You've got to run me as your main to get my Fibonacci goodness")
    print(__name__)

if __name__ == "__main__":
    Main()
elif __name__ == "argumentParser":
    imported()
    


    
