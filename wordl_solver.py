abecedary = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

'''print("Welcome to the word solver!")
print("Remember: gray = 0, yellow = 1, green = 2")
first_word = input("Please enter your first tried word:").upper()
first_word_result = []
first_word_result = input("Please enter your first tried word result separated by commas:")
second_word = input("Please enter your second tried word:").upper()
second_word_result = []
second_word_result = input("Please enter your second tried word result separated by commas:")
third_word = input("Please enter your third tried word:").upper()
third_word_result = []
third_word_result = input("Please enter your third tried word result separated by commas:")
fourth_word = input("Please enter your fourth tried word:").upper()
fourth_word_result = []
fourth_word_result = input("Please enter your fourth tried word result separated by commas:").upper()'''

first_word = 'crate'
first_word_result = [0, 0, 2, 0, 0]
second_word = 'flunk'
second_word_result = [0, 2, 0, 2, 0]
third_word = 'plans'
third_word_result = [0, 2, 2, 2, 0]
fourth_word = 'clans'
fourth_word_result = [0, 2, 2, 2, 0]

first_slot_possible_letters = []
first_slot_definitive_letter = ''
second_slot_possible_letters = []
second_slot_definitive_letter = ''
third_slot_possible_letters = []
third_slot_definitive_letter = ''
fourth_slot_possible_letters = []
fourth_slot_definitive_letter = ''
fifth_slot_possible_letters = []
fifth_slot_definitive_letter = ''


def remove_incorrect_letters():
    for i in range(len(first_word_result)):
        print(first_word_result[i], first_word[i])
        if first_word_result[i] == 0:
            abecedary.pop(i)
        if first_word_result[i] == 1:
            add_possible_letter_to_all_but_one_slot(first_word[i], first_word_result[i])
        if first_word_result[i] == 2:
            print(add_definitive_letter(first_word[i], i))
    print('---------')
    for i in range(len(second_word_result)):
        print(second_word_result[i], second_word[i])
        if second_word_result[i] == 0:
            abecedary.pop(i)
        if second_word_result[i] == 1:
            add_possible_letter_to_all_but_one_slot(second_word[i], second_word_result[i])
        if second_word_result[i] == 2:
            print(add_definitive_letter(second_word[i], i))
    print('---------')
    for i in range(len(third_word_result)):
        print(third_word_result[i], third_word[i])
        if third_word_result[i] == 0:
            abecedary.pop(i)
        if third_word_result[i] == 1:
            add_possible_letter_to_all_but_one_slot(third_word[i], third_word_result[i])
        if third_word_result[i] == 2:
            print(add_definitive_letter(third_word[i], i))
    print('---------')
    for i in range(len(fourth_word_result)):
        print(fourth_word_result[i], fourth_word[i])
        if fourth_word_result[i] == 0:
            abecedary.pop(i)
        if fourth_word_result[i] == 1:
            add_possible_letter_to_all_but_one_slot(fourth_word[i], fourth_word_result[i])
        if fourth_word_result[i] == 2:
            print(add_definitive_letter(fourth_word[i], i))
    return abecedary


def add_possible_letter_to_all_but_one_slot(letter, incorrect_slot):
    if incorrect_slot == 1:
        if letter not in second_slot_possible_letters:
            second_slot_possible_letters.append(letter)
        if letter not in third_slot_possible_letters:
            third_slot_possible_letters.append(letter)
        if letter not in fourth_slot_possible_letters:
            fourth_slot_possible_letters.append(letter)
        if letter not in fifth_slot_possible_letters:
            fifth_slot_possible_letters.append(letter)
    if incorrect_slot == 2:
        if letter not in first_slot_possible_letters:
            first_slot_possible_letters.append(letter)
        if letter not in third_slot_possible_letters:
            third_slot_possible_letters.append(letter)
        if letter not in fourth_slot_possible_letters:
            fourth_slot_possible_letters.append(letter)
        if letter not in fifth_slot_possible_letters:
            fifth_slot_possible_letters.append(letter)
    if incorrect_slot == 3:
        if letter not in first_slot_possible_letters:
            first_slot_possible_letters.append(letter)
        if letter not in second_slot_possible_letters:
            second_slot_possible_letters.append(letter)
        if letter not in fourth_slot_possible_letters:
            fourth_slot_possible_letters.append(letter)
        if letter not in fifth_slot_possible_letters:
            fifth_slot_possible_letters.append(letter)
    if incorrect_slot == 4:
        if letter not in first_slot_possible_letters:
            first_slot_possible_letters.append(letter)
        if letter not in second_slot_possible_letters:
            second_slot_possible_letters.append(letter)
        if letter not in third_slot_possible_letters:
            third_slot_possible_letters.append(letter)
        if letter not in fifth_slot_possible_letters:
            fifth_slot_possible_letters.append(letter)
    if incorrect_slot == 5:
        if letter not in first_slot_possible_letters:
            first_slot_possible_letters.append(letter)
        if letter not in second_slot_possible_letters:
            second_slot_possible_letters.append(letter)
        if letter not in third_slot_possible_letters:
            third_slot_possible_letters.append(letter)
        if letter not in fourth_slot_possible_letters:
            fourth_slot_possible_letters.append(letter)


correct_letters = ['', '', '', '', '']


def add_definitive_letter(letter, correct_slot):
    correct_letters[correct_slot] = letter
    return correct_letters


def create_possible_words():
    possible_words = []
    for i in first_slot_possible_letters:
        for j in second_slot_possible_letters:
            for k in third_slot_possible_letters:
                for l in fourth_slot_possible_letters:
                    possible_words.append(i + j + k + l)
    return possible_words


print(remove_incorrect_letters())
print("first slot possible letters: ", first_slot_possible_letters)
print("second slot possible letters: ", second_slot_possible_letters)
print("third slot possible letters: ", third_slot_possible_letters)
print("fourth slot possible letters: ", fourth_slot_possible_letters)
print("fifth slot possible letters: ", fifth_slot_possible_letters)
print("first slot definitive letter: ", first_slot_definitive_letter)
print("correct letters: ", correct_letters)
print(create_possible_words())
