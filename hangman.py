import random

print("Welcome, guess the word!")

def read_data(filepath="./nouns_list.py"):
    words = []
    with open(filepath, "r") as f:
        for line in f:
            words.append(line.strip().upper())
    return words

def run():
    data = read_data(filepath="./nouns_list.py")
    word = random.choice(data)
    letters_input = []
    opportunities = 6
    done = False

    while not done:
        for letter in word:
            if letter in letters_input:
                print(letter, end=" ")
            else:
                print("_", end=" ") 
        print("\n")
        
        user_answer = input(f"You have {opportunities} opportunities, write a letter: ")
        letters_input.append(user_answer.upper())
        assert user_answer.isalpha(), "You can only try letters"

        if user_answer not in word:
            opportunities -= 1
            if opportunities == 0:
                break
        
        done = True
        for letter in word:
            if letter not in letters_input:
                done = False
        
    if done:
        print("\n")
        print(f"Winner, the word was {word}")
    else:
        print("\n")
        print(f"You lost, the word was {word}")

if __name__ == "__main__":
    run()