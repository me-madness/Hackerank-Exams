# class Car(type):
#     if type =
#
# class Boat:
#     pass
#
# if __name__ == '__main__':
#
#


# Option One
def reverse_words_order_and_swap_cases(sentence: str) -> str:
    # Step 1: Split the sentence into words
    words = sentence.split()

    # Step 2: Reverse the order of the words
    reversed_words = words[::-1]

    # Step 3: Swap the case of each letter in each word
    swapped_case_words = [word.swapcase() for word in reversed_words]

    # Step 4: Join the words back into a single string with spaces
    result_sentence = ' '.join(swapped_case_words)

    return result_sentence


sentence = "rUns dOg"
result = reverse_words_order_and_swap_cases(sentence)
print(result)  # Output: "DoG RUNS"


# Option Two
def reverse_words_order_and_swap_cases(sentence):
    # Step 1: Split the sentence into words
    words = sentence.split()

    # Step 2: Reverse the order of the words
    reversed_words = words[::-1]

    # Step 3: Swap the case of each letter in each word
    swapped_case_words = []
    for word in reversed_words:
        swapped_word = ''.join([char.lower() if char.isupper() else char.upper() for char in word])
        swapped_case_words.append(swapped_word)

    # Step 4: Join the words back into a single string with spaces
    result_sentence = ' '.join(swapped_case_words)

    return result_sentence


sentence = "rUns dOg"
result = reverse_words_order_and_swap_cases(sentence)
print(result)  # Output: "DoG RUNS"