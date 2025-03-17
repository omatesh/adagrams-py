from random import randint

def draw_letters():
    letters_list = []
    pool_of_letters_dict = {
        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 
        'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 
        'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
        }
    
    pool_of_letters_array_TBD = ['A9', 'B2', 'C2', 'D4', 'E12', 'F2', 'G3', 'H2', 'I9', 'J1', 
        'K1', 'L4', 'M2', 'N6', 'O8', 'P2', 'Q1', 'R6', 'S4', 'T6', 
        'U4', 'V2', 'W2', 'X1', 'Y2', 'Z1']

    pool_of_letters_array = []
    for key, value in pool_of_letters_dict.items():
        pool_of_letters_array += list(key) * value

    # print(f"len(pool_of_letters_array:", len(pool_of_letters_array)) #== 98

    i = 0
    while len(letters_list) < 10:
        current_letter_pulled_index = randint(0, len(pool_of_letters_array)-1)
        # print(f"index  number:", current_letter_pulled_index)
        letters_list.append(pool_of_letters_array[current_letter_pulled_index])
        # print(f"final'nij list:", letters_list)
        pool_of_letters_array.pop(current_letter_pulled_index)
        # print(f"(len(pool_of_letters_array):", len(pool_of_letters_array)) # == 88
        i += 1

    #letters_list = ['a','s','g','f','t','w','m','a','u','e'] 10 str elements 
    return letters_list




def uses_available_letters(word, letter_bank):
    # print(f"letter_bank_param:", letter_bank)
    if not word.isalpha():
        return False
    word = word.upper()

    letter_bank_copy = letter_bank[:]

    word_array = list(word)
    for i in range(len(word_array)):
        if word_array[i] in letter_bank_copy:
            letter_bank_copy.remove(word_array[i])
        else:
            return False
    return True

    

def score_word(word):
    score = 0
    score_chart = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }

    if not word.isalpha():
        return False
    word = word.upper()
    
    for letter in word:
        score += score_chart[letter]
        print(f"{letter} and its score {score}")

    if len(word) > 6:
        score += 8
        print(f"added 8 to score")
    
    print(f"{word} and its score {score}")

    return score


def get_highest_word_score(word_list): 
    highest_word_score = 0
    highest_word_score_data = ""
    
    for current_word in word_list:
        current_word_score = score_word(current_word)
        if (highest_word_score < current_word_score) and (len(highest_word_score_data) != 10):
            highest_word_score = current_word_score
            highest_word_score_data = current_word
        
        elif highest_word_score == current_word_score and len(highest_word_score_data) == len(current_word):
            continue

        elif (highest_word_score <= current_word_score) and (len(highest_word_score_data) == 10) and (len(current_word) != 10):
            continue

        elif highest_word_score == current_word_score and len(current_word) == 10:
            highest_word_score = current_word_score
            highest_word_score_data = current_word

        elif highest_word_score == current_word_score and len(highest_word_score_data) > len(current_word):
            highest_word_score = current_word_score
            highest_word_score_data = current_word

    return highest_word_score_data,highest_word_score


# word_list = ["zodiack", "generation", "now", "python"]
# word_list = ["AAAAAAAAAA", "BBBBBB"]
word_list = ["BBBBBB", "AAAAAAAAAA"]
print(get_highest_word_score(word_list))
'''

# letter_bank_global = draw_letters()
# print(f"letter_bank =", letter_bank_global)
# word = "now"
# letter_bank = list("nowdoing")


# word = "resonating"
# word = "resonating"

# word = "AO"
# word = "ao"
# print(f"word:", word)
# letter_bank = list("doing")

# uses_available_letters(word, letter_bank)
# print(uses_available_letters(word, letter_bank_global))


word = "zodiack"
letter_bank_globa = ['g', 'e', 'n', 'e', 'r', 'a', 't', 'i', 'o', 'n'] #"generation"
print(score_word(word))
'''