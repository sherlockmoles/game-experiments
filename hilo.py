import random

response = raw_input("Would you like to play a game? ")

while response == 'y' or "Y":
	target = random.randint(0, 100)
	
	guess = int(raw_input("Choose a number between 1 and 100: "))
	
	while guess != target:
		if guess < target:
			print "Your guess was too low."
			guess = int(raw_input("Guess again: "))
		elif guess > target:
			print "Your guess was too high."
			guess = int(raw_input("Guess again: "))
		
		print "You were right! You win!
		
		response = raw_input("Would you like to play again? ")
		
print "Sorry, I guess I'll see you later."