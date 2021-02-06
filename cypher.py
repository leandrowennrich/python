true = []
false = []
fk = "1234"
end = False


def cypher(key):
    keynum = 0
    for char in key:
        keynum = (keynum + ord(char)) // 2 * 3
    return keynum


def ending():
    global end
    end = True
    return end


def show():
    key = input("Enter a Key: ")
    if key == fk:
        for i in false:
            print(i)
    else:
        keynum = cypher(key)
        for name in true:
            temp = []
            for char in name:
                temp.append(chr(ord(char) - keynum))
            print(''.join(temp))


def add():
    temp = []
    text = input("Enter a text: ")
    wtext = input("Enter a false text: ")
    key = input("Enter a Key: ")
    false.append(wtext)
    keynum = cypher(key)
    for char in text:
        temp.append(chr(ord(char) + keynum))
    true.append(''.join(temp))


commands = {
    'end': ending,
    "show": show,
    "add": add
}

print("Welcome to the Cypher Program! ")
while end == False:
    try:
        command = input("What do you want to do?: ")
        commands[command]()
    except:
        print('''
Not Valid !!!
The valid commands are:
 - add
 - show
 - end
Try again.
''')


print("Thank You!")
