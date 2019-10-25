import argparse


def fib(n):
    a, b = 0, 1   
    for i in range(n):
        a, b = b, a+b
    return a



def Main():  
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help="The supplied number will return the corresponding value in the Fibonacci sequence.", type=int)
    parser.add_argument("-o", "--output", help="Output result to a file", action="store_true")

    args = parser.parse_args()
    answer = fib(args.num)
    print("The " + str(args.num) +"th " + "number in the Fibonacci sequence is " + str(answer))

    if args.output:
        f = open("result.txt", "w+")
        f.write(str(answer))
        f.close()


def imported():
    print("You've got to run me as your main to get my Fibonacci goodness")

if __name__ == "__main__":
    Main()
elif __name__ == "argumentParser":
    imported()
    


    
