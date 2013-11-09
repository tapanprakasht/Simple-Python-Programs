def reverse(text):
    return text[::-1]
def is_palindrome(text):
    return text==reverse(text)
def main():
    string=input("Enter a string:")
    if(is_palindrome(string)):
        print("String is palindrome")
    else:
        print("String is not palindrome")
main()
