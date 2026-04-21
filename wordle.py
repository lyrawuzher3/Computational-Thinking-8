import random

# Pick a word at random
word_list = ["fruit","mango","dream","crazy","happy","angry","image","trust","humor","array","learn","basic","bored","group","class","clean","start","parts","build","grade"]
hidden_word = random.choice(word_list)

#intro
print("Welcome to WORDLE!")
print("Please guess a word:")
print("(your word has to be 5 letters or you  will have to restart the)")
print("(Hint:the word will always be 5 letters long.)")

# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""

    if len(guess_word) == 5:
        print()
    else:
        print("your word is not 5 letters, please restart the program")

    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

        # Second letter (1)
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    # Third letter (2)
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

        # Fourth letter (3)
    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

        # Fifth letter (4)
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        

print(f"You used {i+1} guesses")