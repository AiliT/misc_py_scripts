# check if a string matches the given length, if it does,
# print the LZW code + its length
# (used for assignment, where 20 long string had to be coded into 13 characters)

def spacestr(s):
    os = ''
    for i in range(0, len(s)):
        os += s[i] + ' '
    return os

c = ''
while c.lower() != 'q':
    d = dict()


    il = int(input("Length of input: "))
    s = input(f"{il} long string to test: ")
    os = ''

    if len(s) != il:
        print("Input length doesn't match given number. Please check if you copied \
    the string correctly.")

    else:
        print("Please input the characters of the alphabet (one per line, empty line \
    marks end of input)")
        char = input("Char 1: ")
        c = 1
        while (char != ""):
            d[char] = c
            c += 1
            char = input(f"Char {c}: ")

            
        beg = 0
        end = 1
        
        while beg < il:
            while end <= il and s[beg:end] in d:
                end += 1

            os += str(d[s[beg:end-1]]) + " "
            
            d[s[beg:end]] = c
            c += 1
            beg = end - 1

        print(f"\nThe input:\t{spacestr(s)}\n(length: {il})")
        print(f"The output:\t{os}\n(length: {len(os.split(' ')) - 1})")

    print("\nPress Enter to test another string (write q to quit).")
    c = input('> ')
