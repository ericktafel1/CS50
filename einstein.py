# Define main function, input interger for mass and solve for Energy (measured in Joules)
def main():
    Mass = int(input("Mass (Kilograms): "))
    c = 300000000
    E = Mass * square(c)
    print(f"E: ", E)

# Define square of c
def square(c):
    return pow(c,2)

# Call main function
main()