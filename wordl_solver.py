abecedary = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

first_word = 'crate'
first_word_result = [0, 0, 0, 0, 2]
second_word = 'flunk'
second_word_result = [0, 0, 0, 1, 0]
third_word = 'whips'
third_word_result = [0, 1, 1, 0, 0]
fourth_word = 'boing'
fourth_word_result = [0, 0, 1, 1, 1]

first_word = first_word.upper()
second_word = second_word.upper()
third_word = third_word.upper()
fourth_word = fourth_word.upper()

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


def populate_possible_letters():
    for letter in abecedary:
        first_slot_possible_letters.append(letter)
        second_slot_possible_letters.append(letter)
        third_slot_possible_letters.append(letter)
        fourth_slot_possible_letters.append(letter)
        fifth_slot_possible_letters.append(letter)


def remove_incorrect_letters():
    for i in range(len(first_word_result)):
        if first_word_result[i] == 0:
            if first_word[i] in abecedary:
                abecedary.remove(first_word[i])
        if first_word_result[i] == 1:
            add_possible_letter_to_all_but_one_slot(first_word[i], first_word_result[i])
        if first_word_result[i] == 2:
            add_definitive_letter(first_word[i], i)
    print('---------')
    for i in range(len(second_word_result)):
        print(second_word_result[i], second_word[i])
        if second_word_result[i] == 0:
            if second_word[i] in abecedary:
                abecedary.remove(second_word[i])
        if second_word_result[i] == 1:
            add_possible_letter_to_all_but_one_slot(second_word[i], second_word_result[i])
        if second_word_result[i] == 2:
            add_definitive_letter(second_word[i], i)
    print('---------')
    for i in range(len(third_word_result)):
        print(third_word_result[i], third_word[i])
        if third_word_result[i] == 0:
            if third_word[i] in abecedary:
                abecedary.remove(third_word[i])
        if third_word_result[i] == 1:
            add_possible_letter_to_all_but_one_slot(third_word[i], third_word_result[i])
        if third_word_result[i] == 2:
            add_definitive_letter(third_word[i], i)
    print('---------')
    for i in range(len(fourth_word_result)):
        print(fourth_word_result[i], fourth_word[i])
        if fourth_word_result[i] == 0:
            if fourth_word[i] in abecedary:
                abecedary.remove(fourth_word[i])
        if fourth_word_result[i] == 1:
            add_possible_letter_to_all_but_one_slot(fourth_word[i], fourth_word_result[i])
        if fourth_word_result[i] == 2:
            add_definitive_letter(fourth_word[i], i)
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
    for letter in first_slot_possible_letters:
        for letter2 in second_slot_possible_letters:
            for letter3 in third_slot_possible_letters:
                for letter4 in fourth_slot_possible_letters:
                    for letter5 in fifth_slot_possible_letters:
                        possible_words.append(letter + letter2 + letter3 + letter4 + letter5)
    return possible_words


print(remove_incorrect_letters())
print("first slot possible letters: ", first_slot_possible_letters)
print("second slot possible letters: ", second_slot_possible_letters)
print("third slot possible letters: ", third_slot_possible_letters)
print("fourth slot possible letters: ", fourth_slot_possible_letters)
print("fifth slot possible letters: ", fifth_slot_possible_letters)
print("correct letters: ", correct_letters)
print(create_possible_words())
