#!/bin/python3

# defining a "dictionary" of character families
lower_letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
characters = " !@#$%^&*()_+-=,./?'"

# setting variables
complexity = 0
length = 0
has_duplicates = False

# input and duplicate checking
password = input("Enter a password or passphrase: ")
character_count = {}
for character in password:
	if character in character_count:
		character_count[character] +=1
	else:
		character_count[character] =1
duplicates = [character for character, count in character_count.items() if count >1]
if duplicates:
	duplicates = True
	

# different character families
if any(char in password for char in lower_letters):
	complexity += 1
if any(char in password for char in upper_letters):
	complexity += 1
if any(char in password for char in numbers):
	complexity += 1
if any(char in password for char in characters):
	complexity += 1
if complexity == 4:
	complexity += 1
if duplicates == True:
	complexity -=1

# adding points for length
if len(password) <=8:
	length = 1
elif len(password) <=12:
	length = 2
elif len(password) <=14:
	length =3
elif len(password) > 14:
	length =4
	
# defining strength and recommendations
strength = complexity + length

def Strength():
	print("\n")
	if length <=1:
		print("- 8 character passwords can be cracked by hackers in under an hour, even with uppercase letters, lowercase letters, numbers, and symbols. Consider making your password at least 12 characters in length.")
	elif length <=2:
		print("- Although many sources like NIST say that an 8 character password is sufficient, a 12 character password becomes a lot stronger and harder for hackers to crack. Consider using a longer passphrase instead of a password.")
	elif length <=3:
		print("- A 14 character password or passphrase is very secure, but always remember that the longer the password, the harder it is for hackers to crack it!")
	if complexity == 0:
		print("- Having duplicate characters and no combination of uppercase letters, lowercase letters, numbers, and symbols makes a very weak password and allows hackers to crack passwords very quickly. Consider using a combination of all of these character types.")
	elif complexity < 4 and complexity > 0:
		print("- Strong passwords require using at least one uppercase letter, one lowercase letter, one number, and one symbol in order to make it harder for hackers to guess or crack your password.")
	elif complexity ==4:
		print(" - Your password is pretty complex, but to make it even stronger, consider making sure that your password does not have duplicate letters, numbers, or symbols in order to make it nearly impossible to guess.")

# calling recommendation function and scores		
Strength()

print("\n")
print(f"Strength: {strength}/9")
print(f"Complexity: {complexity}/5")
print(f"Length: {length}/4")
