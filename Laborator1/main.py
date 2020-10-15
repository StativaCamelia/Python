import re


def read_number():
    number_list = []
    while True:
        number = input('Enter number:')
        if not number and len(number_list) >= 2:
            break
        elif not number and len(number_list) < 2:
            print("Nu ati introdus destule numere")
        try:
            number_list.append(int(number))
        except:
            print("Not a number")
    return number_list


def gcd_two(x, y):
    while y:
        x, y = y, x % y
    return x


def gcd_multiple():
    number_list = read_number()
    print([gcd_two(gcd_two(number_list[i-2], number_list[i-1]), number_list[i]) for i in range(2, len(number_list))].pop())


def vowels_string():
    print("Please enter a string:")
    string_test = input()
    print(sum([1 if c in 'aeiou' else 0 for c in string_test.lower()]))


def number_of_occurences():
    print("Please enter first string:")
    string_1 = input()
    print("Please enter second string:")
    string_2 = input()
    print(string_2.count(string_1))


def upperCamel_to_lowerUnderscore():
    print("Please enter the string of characters written in UpperCamelCase:")
    string = input()
    string = re.sub(r'(?!^)(?=[A-Z])', '_', string).lower()
    print(string)


def spiral_matrix():
    matrix = [["f", "i", "r", "s"], ["n", "_", "l", "t"], ["o", "b", "a", "_"], ["h", "t", "y", "p"]]
    row = len(matrix)
    col = len(matrix[0])
    k = 0
    li = 0
    while k < row and li < col:
        for i in range(li, col):
            print(matrix[k][i], end=" ")
        k += 1
        for i in range(k, row):
            print(matrix[i][col - 1], end=" ")
        col -= 1
        if k < row:
            for i in range(col - 1, li - 1, -1):
                print(matrix[row - 1][i], end=" ")
            row -= 1
        if li < col:
            for i in range(row - 1, k - 1, -1):
                print(matrix[i][li], end="")
            li += 1


def palindrom():
    print("Please enter the number:")
    number = input()
    try:
        print("Number is palindrom") if int(number) == int(number[::-1]) else print("Not palindrom")
    except:
        print("Not a number")


def first_number():
    print("Please enter the text:")
    text = input()
    pattern = re.compile(r'\d+')
    print(pattern.findall(text)[0])


def common_character():
    print("Enter Text:")
    text = list(input())
    print(max(list(zip([i for i in text], [text.count(i) for i in text])), key=lambda val: val[1])[0])


def number_of_bytes():
    print("Please enter your number:")
    number = input()
    try:
        count = bin(int(number)).count("1")
        print(count)
    except:
        print("Not a number")


def number_of_words():
    print("Please enter yout text")
    print(len([x for x in input().split() if x != ""]))


if __name__ == '__main__':
    print("Please enter the number of the exercise or 0 if you want to exit:")
    while True:
        option = int(input())
        if option == 1:
            print("Find The greatest common divisor of multiple numbers read from the console.")
            gcd_multiple()
        elif option == 2:
            print("Write a script that calculates how many vowels are in a string.")
            vowels_string()
        elif option == 3:
            print(
                "Write a script that receives two strings and prints the number of occurrences of the first string in "
                "the second.")
            number_of_occurences()
        elif option == 4:
            print(
                "Write a script that converts a string of characters written in UpperCamelCase into "
                "lowercase_with_underscores.")
            upperCamel_to_lowerUnderscore()
        elif option == 5:
            print("Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order (as in the example):")
            spiral_matrix()
        elif option == 6:
            print("Write a function that validates if a number is a palindrome.")
            palindrom()
        elif option == 7:
            print("Write a function that extract a number from a text (for example if the text is An apple is 123 USD, this function will return 123, or if the text is abc123abc the function will extract 123). The function will extract only the first number that is found.")
            first_number()
        elif option == 8:
            print("Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format is 00011000, meaning 2 bits with value 1")
            number_of_bytes()
        elif option == 9:
            common_character()
        elif option == 10:
            number_of_words()