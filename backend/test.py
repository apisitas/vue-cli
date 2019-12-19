import re


def check_letter(letters):
    text = ""
    if letters.isupper():
        text = "All Capital Letter"
    if letters.islower():
        text = "All Small Letter"

    uppers = [l for l in letters if l.isupper()]
    lowers = [l for l in letters if l.islower()]
    if uppers and lowers:
        text = "Mix"

    regex = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
    if regex.search(letters):
        text = "Invalid Input"
    print(text)


check_letter("asdfHRbySFss")
