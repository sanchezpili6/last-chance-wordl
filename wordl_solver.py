possible_letters = ['Q', 'O', 'A', 'D', 'J', 'Z', 'X', 'V', 'M']
current_known_letters = [None, 'A', 'D', None, None]
not_first_letters = ['Q','O','A','D','J', 'Z']


def find_five_slot_combinations(possible_letters):
    """
    Find all possible combinations of five letters.
    """
    combinations = []
    for letter1 in possible_letters:
        for letter2 in possible_letters:
            for letter3 in possible_letters:
                for letter4 in possible_letters:
                    for letter5 in possible_letters:
                        combinations.append(letter1 + letter2 + letter3 + letter4 + letter5)
    return combinations


def filter_combinations(combinations, current_known_positions, known_positions):
    """
    Filter out combinations that don't match the current known positions.
    """
    words = []
    for combination in combinations:
        if combination[1] == current_known_positions[1] and combination[2] == current_known_positions[2] and combination[0] not in not_first_letters:
            words.append(combination)
    return words


def get_known_possitions(current_known_positions):
    """
    Get the known positions from the current known positions.
    """
    known_positions = []
    for p in range(len(current_known_positions)):
        if p is not None:
            known_positions.append(p)
    return known_positions


def print_filtered_combinations(words):
    """
    Print the filtered combinations.
    """
    for word in words:
        print(word)

