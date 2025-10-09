from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

birthday = input("enter your birthday, in the form mmddyy:")
if birthday in pi_string:
    print("your birthday appears in the first million digits of pi!")
else:
    print("your birthday does not appear in the first million digits of pi.")
