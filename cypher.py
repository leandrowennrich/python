# Create a true and a false list
true_list = []
false_list = []

# Create a false key to return the fake values
false_key = "1234"

# Keep the program looping
end = False

# Return a number from a String keyword


def cypher(key):
    keynum = 0
    for char in key:
        keynum = keynum + ord(char) // 2 * 3
    return keynum

# Finish the program


def ending():
    global end
    end = True
    return end

# Show the list values.
# If you pass tha flase key, it will show tha fake list,
# if you pass a random key. it will return a incrypted list.


def show():
    key = input("Enter a Key: ")
    if key == false_key:
        for i in false_list:
            print(i)
    else:
        keynum = cypher(key)
        for name in true_list:
            # A temporary list to hold the individual character value
            temp = []
            for char in name:
                temp.append(chr(ord(char) - keynum))
            print(''.join(temp))


def add():
    # A temporary list to hold the individual character value
    temp = []
    # Pass the real word
    right_text = input("Enter a text: ")
    # Pass a wrong word
    wrong_text = input("Enter a false text: ")
    # pass the key to Encrypt the Right word
    key = input("Enter a Key: ")
    false_list.append(wrong_text)
    keynum = cypher(key)
    for char in right_text:
        temp.append(chr(ord(char) + keynum))
    true_list.append(''.join(temp))


# A Dictionary to call a function from the inputed String
commands = {
    'end': ending,
    "show": show,
    "add": add
}
# Main program
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
