import sys
import time


def letter_converter(word):
    word = word.replace("İ", "i")
    word = word.replace("I", "ı")
    return word.lower()


def file_handling(args):
    # Open files and create dictionaries.
    if len(args) != 3:
        print("You must write two arguments for this program")
        return False
    word_keys_temp = []
    word_dict_temp = dict()
    letter_values_temp = dict()
    with open(args[1], "r", encoding="utf8") as words:
        for line in words:
            # Skip if the line is empty.
            if line != "\n":
                temp_list = (line.split(":")[1].strip("\n")).split(",")
                temp_list = [letter_converter(i) for i in temp_list]
                word_keys_temp.append(letter_converter(line.split(":")[0]))
                word_dict_temp[letter_converter(line.split(":")[0])] = temp_list
    with open(args[2], "r", encoding="utf8") as letters:
        for letter in letters:
            if letter != "\n":
                letter_values_temp[letter_converter(letter.split(":")[0])] = letter.split(":")[1].strip("\n")
    return word_dict_temp, letter_values_temp, word_keys_temp


def score_function(letter_values_parameter, guess):
    # Calculate the point of a word.
    point = 0
    letter_list = list(guess)
    for i in letter_list:
        point += int(letter_values_parameter[i])
    return point * len(letter_list)


def main_loop(words_dict, letter_values_parameter, word_keys_parameter):
    while len(word_keys_parameter) > 0:
        score = 0
        guess_list = []
        # Delete and return shuffled word from dictionary.
        shuffled = word_keys_parameter.pop(0)
        start = time.time()
        remaining_time = 30
        print("Shuffled letters are:", shuffled, "Please guess words for these letters with minimum three letters")
        # Check time and whether every word is guessed
        while remaining_time > 0 and len(guess_list) < len(word_dict[shuffled]):
            guess = letter_converter(input("Guessed word: "))
            end = time.time()
            remaining_time = (30 - int(end - start))
            if guess in guess_list:
                print("This word is guessed before")
            elif guess not in words_dict[shuffled]:
                print("your guessed word is not a valid word")
            elif remaining_time > 0:
                score += score_function(letter_values_parameter, guess)
                guess_list.append(guess)
            if remaining_time > 0:
                print("You have  %d  time" % (remaining_time,))
            else:
                print("You have  0  time")
        print("Score for  %s  is  %d and guessed words are:" % (shuffled, score), "-".join(guess_list))


word_dict, letter_values, word_keys = file_handling(sys.argv)
main_loop(word_dict, letter_values, word_keys)
