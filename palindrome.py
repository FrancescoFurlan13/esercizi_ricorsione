def palindorme(word):
    if len(word)<=1:
        return True
    else:
        return word[0]==word[-1] and palindorme(word[1:-1])

def palindrome_banale(word):
    return word==word[::-1]

if __name__ == '__main__':
    print(palindorme("anna"))
    print(palindrome_banale("panna"))
    print(palindrome_banale("tonno"))
    print(palindrome_banale("oro "))