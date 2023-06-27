# D:/Cde/Python/Pap/Lessons/Part_02/Files/test.txt

command = input("Please enter cooman 'Read' or 'Copy' ")

if command.lower() == "read":
    path = input("Write the path to the file whose content you want to view:")
    data = open(path, 'r')
    print(data.read())
    data.close()
elif command.lower() == "copy":
    copypath = input("Write the path to the file you want to copy:")
    data = open(copypath, 'r')
    text = data.read()
    data.close()
    new = open("D:/Cde/Python/Pap/Lessons/Part_02/test.txt", 'w')
    new.write(text)
    new.close()
    new = open("D:/Cde/Python/Pap/Lessons/Part_02/test.txt", 'r')
    print(new.read())
    new.close()




