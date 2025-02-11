with open("output.py", "w") as file:
    file.write("i = int(input('Choose a number: '))\n")

    for i in range(2**32):
        if i % 2 == 0:
            file.write("if i == " + str(i) + ":\n")
            file.write("    print('even')\n")
        elif i % 2 != 0:
            file.write("if i == " + str(i) + ":\n")
            file.write("    print('odd')\n")