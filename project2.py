# beginning: create variables
talkative_points = 0
in_between_points = 0
quiet_points = 0

# intro
print("WELCOME TO THE PERSONALITY QUIZ!!!")
input()
name = input("What is your name?   ")
print("")
print(f"Welcome {name}! Let's get started!")
input()

# question 1
print("")
answer1 = input("First question: Do you consider yourself A an extrovert B an ambivert or C an introvert?   ")
if answer1 == "A" or answer1 == "a":
    talkative_points += 1
elif answer1 == "B" or answer1 == "b":
    in_between_points += 1
elif answer1 == "C" or answer1 == "c":
    quiet_points += 1
else:
    print("Sorry, you can only answer A, a, B, b, C, and c... you're result will be inconclusive...")

# question 2
print("")
answer2 = input("Second question: Ask a friend if you are A quiet B loud or C in between?   ")
if answer2 == "B" or answer2 == "b":
    talkative_points += 1
elif answer2 == "C" or answer2 == "c":
    in_between_points += 1
elif answer2 == "A" or answer2 == "a":
    quiet_points += 1
else:
    print("Sorry, you can only answer A, a, B, b, C, and c... you're result will be inconclusive...")

# question 3
print("")
answer3 = input("Third question: Do you prefer to be A alone B with friends or C with family   ")
if answer3 == "B" or answer3 == "b":
    talkative_points += 1
elif answer3 == "C" or answer3 == "c":
    in_between_points += 1
elif answer3 == "A" or answer3 == "a":
    quiet_points += 1
else:
    print("Sorry, you can only answer A, a, B, b, C, and c... you're result will be inconclusive...")

# question 4
print("")
answer4 = input("Fourth question: Do you prefer A dogs B cats or C other?   ")
if answer4 == "A" or answer4 == "a":
    talkative_points += 1
elif answer4 == "C" or answer4 == "c":
    in_between_points += 1
elif answer4 == "B" or answer4 == "b":
    quiet_points += 1
else:
    print("Sorry, you can only answer A, a, B, b, C, and c... you're result will be inconclusive...")

# question 5
print("")
answer5 = input("Fifth question: What do you prefer to do with your friends? A video games B shopping or C just chill and hangout? ")
if answer5 == "A" or answer5 == "a":
    talkative_points += 1
elif answer5 == "B" or answer5 == "b":
    in_between_points += 1
elif answer5 == "C" or answer5 == "c":
    quiet_points += 1
else:
    print("Sorry, you can only answer A, a, B, b, C, and c... you're result will be inconclusive...")

# question 6
print("")
answer6 = input("Last question: What do you think you will get A quiet B talkative or B in between? ")
if answer6 == "A" or answer6 == "a":
    talkative_points += 1
elif answer6 == "B" or answer6 == "b":
    in_between_points += 1
elif answer6 == "C" or answer6 == "c":
    quiet_points += 1
else:
    print("Sorry, you can only answer A, a, B, b, C, and c... you're result will be inconclusive...")

# results
print("Here are your results:")
if talkative_points > in_between_points and talkative_points > quiet_points:
    print("You are a talkative person! You love to hangout with your friends and you give off energy to the people around you!")
if in_between_points > talkative_points and in_between_points > quiet_points:
    print("You are a little bit of everything! You tend to be quiet sometimes but you are selectively talkative to the people you know and love! You're not too much and you're not too little!")
if quiet_points > talkative_points and quiet_points > in_between_points:\
    print("You are quiet and observant! You tend to be a little less social but you are nice and caring!")