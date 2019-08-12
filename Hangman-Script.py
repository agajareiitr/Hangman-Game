import time #imported time module
import random

name=input("May I have Your Name please : ")

print(f"Hello {name} Time to play Hangman\n")

def get_a_random_word():
	file=open("dataSet.txt","r")
	random_word=random.choice(file.readlines())
	file.close()
	return random_word
def check(word,guesses,guess):
	status=''
	matches=0
	for letter in word:
		if letter in guesses:
			status+=letter
		else:
            status+=" _ "
		if letter==guess:
			matches+=1
	if matches>1:
		print(f"Yoo! the word has {matches} '{guess}'s")
	elif matches==1:
		print(f"Yup, the word has '{guess}'")
	else:
		print(f"Sorry but the word does not contain the letter '{guess}'")
	return status

def main():
	word=get_a_random_word()
	guesses=[]
	guessed=False
	print(f"The word contains {len(word)} letters\n")
	print("Note: All letter should be given in lowercase\n")
	while not guessed:
		text="Now lets enter a letter : "
		guess=input(text)
		if guess in guesses:
			print(f"You already guessed '{guess}' ")
		elif len(guess)==len(word):
			if guess==word:
				guessed=True
			else:
				print("Sorry, that is incorrect guess")
		elif len(guess)==1:
			guesses.append(guess)
			result =check(word,guesses,guess)
			if result==word:
				guessed=True
			else:
				print(result)
		else:
			print("Invalid entry")
	print(f"yes, the word is {word} ! You have got it in {len(guesses)} tries.")
main()
