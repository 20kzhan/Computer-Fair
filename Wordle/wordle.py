with open("word_list.txt.txt", 'r') as word_list:
    word_list = [s.replace('\n', '') for s in word_list.readlines()]
with open("all_words.txt", 'r') as valid_words:
    valid_words = [w.lower() for w in valid_words.readlines()[0].split(' ')]
    valid_words[-1] = valid_words[-1]

guess = input("Enter the first guess: ")
correct_letters =