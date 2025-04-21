# Step 1: Create and write to input.txt
with open("input.txt", "w") as file:
    file.write("Learning Python is fun.\n")
    file.write("Files can be read and written easily.\n")
    file.write("This line adds more content.\n")
    file.write("Python is powerful for data processing.\n")
    file.write("Let’s process this text file.\n")
print("Step 1 complete: input.txt created.")

# Step 2: Read from input.txt
with open("input.txt", "r") as file:
    content = file.read()
print("Step 2 complete: Read from input.txt.")

# Step 3: Count the number of words
word_count = len(content.split())
print(f"Step 3 complete: Word count = {word_count}")

# Step 4: Convert text to uppercase
content_upper = content.upper()
print("Step 4 complete: Converted text to uppercase.")

# Step 5: Write to output.txt
with open("output.txt", "w") as file:
    file.write(content_upper)
    file.write(f"\n\nWORD COUNT: {word_count}\n")
print("Step 5 complete: output.txt written.")

# Step 6: Print success message
print("File processed successfully. 'output.txt' has been created.")
