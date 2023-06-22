handler = open('Files/test.txt', 'a')
handler.write('abc\n456')
handler.close()

handler = open('Files/test.txt', 'r')
print(handler.read(2))
handler.seek(0)
print(handler.read())

for line in handler:
    print(line)
handler.close()

file = 'b.txt'

while True:
    print('1 - Write to the file; 2 - Read the file; 0 - Exit ')
    ini = input('Enter command: ')
    if ini =='0':
        exit(0)
    elif ini =='1':
        text = input('Enter line: ')
        handler = open(file, 'w')
        handler.write(text)
        handler.close()
    elif ini == '2':
        try:
            handler = open(file, 'r')
            print(handler.read())
            handler.close()
        except FileNotFoundError:
            print('File does not exist!')
    else:
        print('Unknown command! ')






