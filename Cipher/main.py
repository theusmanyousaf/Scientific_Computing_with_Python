text = 'Hello World' # text variable of type 'str'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)  # print is a built in function to see output on console
shifted = alphabet[index + shift]
print(shifted)