#name code
print("Hello there! What is your name?")
my_name = input()
print("Nice to meet you " + my_name + " My name is Not A. Bot. If you want to leave, just press Q")
quit_character = 'q'
if my_name == 'q':
  print("Goodbye")
  exit()

#what you want to talk about, need to type it right the first time
print("So, " + my_name + "what do you want to talk about, we can talk about your favorite animal, activity, and food!")
talkAbout = input()
if talkAbout == 'q':
  print("Goodbye")
  quit()

if talkAbout == 'animals':
  favAnimal = input("What is your favorite animal?\n")
  if favAnimal == 'q':
    print("Goodbye")
    exit()
  print("That's cool! I also love " + favAnimal)

elif talkAbout == 'activities':
  favActivity = input("What is your favorite activity?\n")
  if favActivity == 'q':
    print('Goodbye')
  print("Hmm, that sounds like fun!")
elif talkAbout == 'food':
  favFood = input("What is your favorite food?\n")
  if favFood == 'q':
    print("Goodbye")
    quit()
  print("Man, that sounds delicious!")
else:
  print('I\'m sorry, but I didn\'t understand that. Could you restart and try again?')
print("What else do you want to talk about? We can talk about either school or books!")

#secodn option of talking 
moreTalking = input()
if moreTalking == 'q':
  print("Goodbye!")
  quit()
if moreTalking == 'school':
  schoolSubject = input("What is your favorite school subject?\n")
  if schoolSubject == 'q':
    print("Goodbye!")
    quit()
  print("Man, " + schoolSubject + " sounds like fun!")
elif moreTalking =='books':
  favBook = input("What is your favorite book?\n")
  if favBook == 'q':
    print("Goodbye")
    quit()
  print("That sounds like a good read!")
print("Sorry, but I have to go now! Talk to you soon!")
quitCode = input("Please press q to quit")
if quitCode == 'q':
  print("See you soon!")
  quit()