data = input("Enter some data: ")

with open("output.txt", "w") as file:
    file.write(data + "\n")

print("Data written successfully.")


extra_data = input("Enter additional data to append: ")

with open("output.txt", "a") as file:
    file.write(extra_data + "\n")

print("Additional data appended successfully.")


print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)