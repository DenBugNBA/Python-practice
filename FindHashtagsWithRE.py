import re

text = input("Enter the text: ")

for i in re.findall("#\w+", text):
    print(i)
