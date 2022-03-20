import random
import copy

def replace(alist, index, char):
    if isinstance(index, list):
        for i in index:
            alist.pop(i)
            alist.insert(i, char)
    else:
        alist.pop(index)
        alist.insert(index, char)

def print_list(alist, end=''):
    for c in alist:
        print(c, end=end)
    print('\n')

def format_list(alist, end=''):
    formatted = ''

    for c in alist:
        formatted += c + end
    return formatted

def print_rules():
    pass

def play_game():
    diff = input("1. Easy\n2. Hard\n\nSelect a difficulty: ")
    if diff == "1":
        with open("Hangman/easy_words.txt", "r") as easy_words:
            word_list = [w.replace("\n", "") for w in easy_words.readlines()]
    elif diff == "2":
        with open("Hangman/hard_words.txt", "r") as hard_words:
            word_list = [w.replace("\n", "") for w in hard_words.readlines()]

    selected_word = random.choice(word_list)

    word = []
    word[:0] = selected_word

    total_guesses = ['_'] * len(word)

    wrong_letters = []

    while total_guesses != word:
        print(f"Wrong letters: ", end='')
        print_list(wrong_letters, ' ')
         
        print_list(total_guesses)

        guess = input("Pick a letter: ")
        if guess not in wrong_letters:
            if not guess.isalpha() and len(guess) != 1:
                print("Invalid letter.")
            elif guess not in word:
                print(f"{guess.upper()} is wrong.")
                wrong_letters.append(guess)
            else:
                print(f"{guess.upper()} is correct!")
                # find all locations of the letter
                locations = []

                temp_word = copy.copy(word)
                
                for c in word:
                    try:
                        locations.append(temp_word.index(guess))
                        temp_word.remove(guess)
                    except ValueError:
                        pass
                # locations = list(set(locations))
                for i in range(len(locations)):
                    locations[i] = locations[i] + i
                
                # replace the _ with the letter
                replace(total_guesses, locations, guess)
                
        else:
            print(f"You already tried {guess}.")
        print()
    print(f"You Win! The word was {format_list(word)}.")


if __name__ == '__main__':
    play_game()