# Define main function, ask input of x and print squared x
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

# Define square function, return squared x --- n is x and 2 is exponent
def square(n):
    return pow(n, 2)

# Call main function
main()
