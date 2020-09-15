import string
def pangram(string):
	alphabet="abcdefghijklmnopqrstuvwxyz"
	for char in alphabet:
		if char not in string:
			return False
		return True
string="five boxing wizards jump quickly"
if(pangram(string)==True):
	print("given string is pangram")
else:
	print("string is not a pangram")