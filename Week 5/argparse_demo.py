import argparse

def main(arguments):
    # if verbose
    #print out numbers and operation
    if arguments.verbose:
        print(f"Operands are {args.num1} and {args.num2}.")
        print(f"Selected operation is  {args.operation}.")    
    #if operation is add
    #add numbers
    elif args.operation == 'add':
        result =args.num1 + args.num2
        print("Result is : ",result)

    #if operation is subtract
    #subtract numbers
    elif args.operation == 'subtract':
        result =args.num1 - args.num2
        print("Result is : ",result)
    #if multiply
    #mult numbers
    elif args.operation == 'multiply':
        result =args.num1 * args.num2
        print("Result is : ",result)
    #if divide
    #check for divide by 0
    elif args.operation == 'divide':
        if args.num2 == 0:
            print("Error:cannot divide by zero")
            exit()
        result =args.num1 / args.num2
        print("Result is : ",result)
    #divide numbers
    #else
    #error message about unsupported operation
    else:
        print(f"Error: {args.operation} is an unsupported operation")

if __name__ == '__main__':
    # set up argument parser
    parser = argparse.ArgumentParser(description="command line calculator")

    #add args
    #positional args
    parser.add_argument('num1',type=float,help='input first number')
    parser.add_argument('num2',type=float,help="input second number")

    #optional args
    parser.add_argument('-o','--operation',type=str,default='add',help="math operation from [add, subtract, multiply, divide]")
    parser.add_argument("-v","--verbose",action='store_true', help="increase output")
    #parse args
    args = parser.parse_args()
    #call main functions
    main(args)