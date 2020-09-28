import collections
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    """
    Question: Write a program which takes text for an anonymous LETTER and text for a MAGAZINE and determine if it is
              possible to write the anonymous letter using the magazine which means if any character occurs more often
              in the LETTER than the MAGAZINE we return FALSE.
    Solution:
        To write the letter using chars from magazine, then the char count of letter should be a SUBSET of the
        count of the magazine which means magazine should bigger than letter. Therefore, if we subtract the bigger
        from the smaller, the resulting Counter should be of length ZERO, as SUBTRACTING will only keep the
        POSITIVE ones.
    Time Complexity: O(L + M) where L & M are number of characters in Letter and Magazine respectively.
    Space Complexity: O(C) where C is number of DISTINCT characters in .... ??

    """
    # letter_counter = collections.Counter(letter_text)
    # magazine_counter = collections.Counter(magazine_text)
    # diff_counter = letter_counter - magazine_counter
    # return len(diff_counter) == 0

    return len(collections.Counter(letter_text)) - len(collections.Counter(magazine_text)) == 0

if __name__ == "__main__":
    letter = "hello world how are you"
    magazine = "hello hello world you are how"
    result = is_letter_constructible_from_magazine(letter, magazine)
    print(result) # True

    letter = "hello world how are you, k"
    magazine = "hello hello world you are how"
    result = is_letter_constructible_from_magazine(letter, magazine)
    print(result) # False