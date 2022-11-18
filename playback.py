# Define main function, ask for input and call it slow
def main():
    slow = str(input("Say something and I will repeat it slowly to you! "))
    # Print slow and replace spaces with ...
    print(slow.replace(" ","..."))

# Call main function
main()