def pallindrome_2019_1_60_209(line):
    line = line.lower()
    if line == line[::-1]:
        return 1
line = str(input("Enter a word: "))

if pallindrome_2019_1_60_209(line) == 1:
    print(line, "is pallindrome.")
else:
    print(line, "is not pallindrome.")