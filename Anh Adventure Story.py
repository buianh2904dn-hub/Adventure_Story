import random
import time

time.sleep(1)
print("Once upon a time, there was a really valuable treasure which hided inside the center of a mountain.")
time.sleep(2)
print("Every hunters always want to hunt for that treasure and make it belong to them.")
time.sleep(2)
print("However, that mountain is also the home of a mysterious monster which kill every hunters if they just missed their step to its territory.")
time.sleep(2)
print("YOU - are a hunter on the way to looking for that treasure to help yourself.")
time.sleep(2)
print("After passing through the primeval jungle and killing some little monsters, you are now faced with a very difficult choice...")
time.sleep(2)
print("LEFT or RIGHT?")
time.sleep(2)
print("A big sign which lead you to the way of DEAD be eaten by a monster OR a way to become the RICHEST person in the world.")
time.sleep(2)
print("So")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")


def ask1():
	ques_1 = 0
	lcounter = 0
	hcounter = 0
	while ques_1 > 2 or ques_1 < 1: 
		ques_1 = int(input("What is your choice? ( 1 = right ; 2 = left) \n"))
			
		if hcounter == 1:
			print("Impossible. Please choose only 1 or 2 to decided.")
		elif lcounter == 1:
			print("Impossible. Please choose only 1 or 2 to decided.")
		return ques_1
		if ques_1 < 1:
			lcounter += 1
		elif ques_1 > 2:
			hcounter += 1
	return ques_1

again = 'yes'
while again == 'yes' or again == 'y':
	num = random.randint(1, 2)
	choice = ask1()
	if choice == 'again':
		again = input("Do you want to play again?").lower()
	else:
		if num == 1:
			if choice == num:
				time.sleep(2)
				print("You currently walking through a small, wet cave...")
				time.sleep(2)
				print("The way too dark that you couldn't see anything around. And suddenly...")
				time.sleep(2)
				print("A beautiful, classic door suddenly appear in front of you.")
				time.sleep(2)
				print("Because of curious...")
				time.sleep(2)
				print("You open the door without thinking what happened inside.")
				time.sleep(2)
				print("It could be a monster that killed a bunch of brave hunters that went to hunt the treasure before.")
				time.sleep(2)
				print("And ... BOOM!!!!")
				time.sleep(2)
				print("CONGRATULATIONS!!! THE TREASURE NOW IS YOURS!!!")
			else:
				if choice >= 3 or choice <= 0:
					ask1()
					if choice == num:
						time.sleep(2)
						print("You currently walking through a small, wet cave...")
						time.sleep(2)
						print("The way too dark that you couldn't see anything around. And suddenly...")
						time.sleep(2)
						print("A beautiful, classic door suddenly appear in front of you.")
						time.sleep(2)
						print("Because of curious...")
						time.sleep(2)
						print("You open the door without thinking what happened inside.")
						time.sleep(2)
						print("It could be a monster that killed a bunch of brave hunters that went to hunt the treasure before.")
						time.sleep(2)
						print("And ... BOOM!!!!")
						time.sleep(2)
						print("CONGRATULATIONS!!! THE TREASURE NOW IS YOURS!!!")
						
					else:
						if choice >= 3:
							time.sleep(2)
							print("As you type 2 times integers that higher than 2")
							time.sleep(2)
							print("The story right now will be ended.")
						elif choice <= 0:
							time.sleep(2)
							print("As you type 2 times intgers that lower than 1")
							time.sleep(2)
							print("The story right now will be ended.")
						else:
							time.sleep(2)
							print("You currently walking through a small, wet cave...")
							time.sleep(2)
							print("The way too dark that you couldn't see anything around. And suddenly...")
							time.sleep(2)
							print("A beautiful, classic door suddenly appear in front of you.")
							time.sleep(2)
							print("Because of curious...")
							time.sleep(2)
							print("You open the door without thinking what happened inside.")
							time.sleep(2)
							print("It could be a monster that killed a bunch of brave hunters that went to hunt the treasure before.")
							time.sleep(2)
							print("And ... BOOM!!!!")
							time.sleep(2)
							print("A monster's currently sleeping with a hungry stomach")
							time.sleep(2)
							print("It's waiting for a long time to eat and now, you woke it up.")
							time.sleep(2)
							print("You tried to ran so fast just to escape away from that monster BUT...")
							time.sleep(2)
							print("The monster catched you.")
							time.sleep(2)
							print("NOW YOU DEAD HAHAHAHAHAHAHAHAHAHA")
						
				else:
					time.sleep(2)
					print("You currently walking through a small, wet cave...")
					time.sleep(2)
					print("The way too dark that you couldn't see anything around. And suddenly...")
					time.sleep(2)
					print("A beautiful, classic door suddenly appear in front of you.")
					time.sleep(2)
					print("Because of curious...")
					time.sleep(2)
					print("You open the door without thinking what happened inside.")
					time.sleep(2)
					print("It could be a monster that killed a bunch of brave hunters that went to hunt the treasure before.")
					time.sleep(2)
					print("And ... BOOM!!!!")
					time.sleep(2)
					print("A monster's currently sleeping with a hungry stomach")
					time.sleep(2)
					print("It's waiting for a long time to eat and now, you woke it up.")
					time.sleep(2)
					print("You tried to ran so fast just to escape away from that monster BUT...")
					time.sleep(2)
					print("The monster catched you.")
					time.sleep(2)
					print("NOW YOU DEAD HAHAHAHAHAHAHAHAHAHA")
	
		else:
			if choice == num:
				time.sleep(2)
				print("You currently walking through a small, wet cave...")
				time.sleep(2)
				print("The way too dark that you couldn't see anything around. And suddenly...")
				time.sleep(2)
				print("A beautiful, classic door suddenly appear in front of you.")
				time.sleep(2)
				print("Because of curious...")
				time.sleep(2)
				print("You open the door without thinking what happened inside.")
				time.sleep(2)
				print("It could be a monster that killed a bunch of brave hunters that went to hunt the treasure before.")
				time.sleep(2)
				print("And ... BOOM!!!!")
				time.sleep(2)
				print("CONGRATULATIONS!!! THE TREASURE NOW IS YOURS!!!")
			else:
				if choice >= 3 or choice <= 0:
					ask1()
					if choice == num:
						time.sleep(2)
						print("You currently walking through a small, wet cave...")
						time.sleep(2)
						print("The way too dark that you couldn't see anything around. And suddenly...")
						time.sleep(2)
						print("A beautiful, classic door suddenly appear in front of you.")
						time.sleep(2)
						print("Because of curious...")
						time.sleep(2)
						print("You open the door without thinking what happened inside.")
						time.sleep(2)
						print("It could be a monster that killed a bunch of brave hunters that went to hunt the treasure before.")
						time.sleep(2)
						print("And ... BOOM!!!!")
						time.sleep(2)
						print("CONGRATULATIONS!!! THE TREASURE NOW IS YOURS!!!")
					else: 
						if choice >= 3:
							time.sleep(2)
							print("As you type 2 times integers that higher than 2")
							time.sleep(2)
							print("The story right now will be ended.")
						elif choice <= 0:
							time.sleep(2)
							print("As you type 2 times intgers that lower than 1")
							time.sleep(2)
							print("The story right now will be ended.")
						else:
							time.sleep(2)
							print("You currently walking through a small, wet cave...")
							time.sleep(2)
							print("The way too dark that you couldn't see anything around. And suddenly...")
							time.sleep(2)
							print("A beautiful, classic door suddenly appear in front of you.")
							time.sleep(2)
							print("Because of curious...")
							time.sleep(2)
							print("You open the door without thinking what happened inside.")
							time.sleep(2)
							print("It could be a monster that killed a bunch of brave hunters that went to hunt the treasure before.")
							time.sleep(2)
							print("And ... BOOM!!!!")
							time.sleep(2)
							print("A monster's currently sleeping with a hungry stomach")
							time.sleep(2)
							print("It's waiting for a long time to eat and now, you woke it up.")
							time.sleep(2)
							print("You tried to ran so fast just to escape away from that monster BUT...")
							time.sleep(2)
							print("The monster catched you.")
							time.sleep(2)
							print("NOW YOU DEAD HAHAHAHAHAHAHAHAHAHA")
				else:
					time.sleep(2)
					print("You currently walking through a small, wet cave...")
					time.sleep(2)
					print("The way too dark that you couldn't see anything around. And suddenly...")
					time.sleep(2)
					print("A beautiful, classic door suddenly appear in front of you.")
					time.sleep(2)
					print("Because of curious...")
					time.sleep(2)
					print("You open the door without thinking what happened inside.")
					time.sleep(2)
					print("It could be a monster that killed a bunch of brave hunters that went to hunt the treasure before.")
					time.sleep(2)
					print("And ... BOOM!!!!")
					time.sleep(2)
					print("A monster's currently sleeping with a hungry stomach")
					time.sleep(2)
					print("It's waiting for a long time to eat and now, you woke it up.")
					time.sleep(2)
					print("You tried to ran so fast just to escape away from that monster BUT...")
					time.sleep(2)
					print("The monster catched you.")
					time.sleep(2)
					print("NOW YOU DEAD HAHAHAHAHAHAHAHAHAHA")


		again = input("Do you want to play again? \n").lower()

print("Thanks for reading")






