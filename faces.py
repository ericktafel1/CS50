# Define main function asking for input emotion to convert to emoji
def main():
    face = str(input("How are you feeling today? "))
    # Call the convert function
    result = convert(face)
    # Print result of convert function
    print(result)

def convert(face):
    # Replace :)
    face1 = face.replace(":)", "🙂")
    # Replace :(, chained with face1
    face2 = face1.replace(":(", "🙁")
    # Return string
    return face2

# Call main function
main()