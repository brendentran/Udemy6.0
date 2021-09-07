def is_palindrome(string):
    backwards = string[::-1].casefold()
    return backwards == string.casefold()


def palindrome_sentence(sentence):
    string =  ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    #return string [::-1].casefold() == string.casefold()
    return is_palindrome(string)


sentence = input("Please enter a sentence to check: ")
if palindrome_sentence(sentence):
    print("'{}' is a palindrome".format(sentence))
else:
    print("'{}' is not a palindrome".format(sentence))

