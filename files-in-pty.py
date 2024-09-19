

# File Creation
try:
    # Open a file named "my_file.txt" in write mode ('w')
    with open('my_file.txt', 'w') as file:
        # Write three lines of text to the file
        file.write("This is the first line of text.\n")
        file.write("Here is the second line, which includes a number: 42\n")
        file.write("And this is the third line with more text.\n")

    print("File created and data written successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while creating or writing to the file: {e}")

# File Reading and Display
try:
    # Open the file in read mode ('r')
    with open('my_file.txt', 'r') as file:
        # Read the contents of the file
        content = file.read()
        # Display the contents on the console
        print("\nFile Contents:")
        print(content)

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while reading the file: {e}")

# File Appending
try:
    # Open the file in append mode ('a')
    with open('my_file.txt', 'a') as file:
        # Append three additional lines of text
        file.write("Appending a new line to the file.\n")
        file.write("Here's another appended line with a number: 99\n")
        file.write("Final appended line with some more text.\n")

    print("\nAdditional lines appended successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while appending to the file: {e}")

finally:
    print("\nFile handling operations complete.")
