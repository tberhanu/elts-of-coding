def find_all_substrings(words, sentence):
    """
    Taking a SENTENCE and a list of WORDS, find the substring of the sentence which are the concatenation of all
    the words in ANY ORDER.
    Input:
        words = ["can", "apl", "ana"]
        sentence = "amanaplanacanal"
    Output: index: 4 as the substring is "aplanacan"

    Input:
        words = ["can", "apl", "ana"]
        sentence = "amanaplanacaanaaplcanl"
    Output: index: 12 as the substring is "anaaplcan"

    Tess Strategy: First get the length of all the concatenated words, and only compare a slice from the sentence
                   with the same length: O(N * W) where N is len(sentence), and W len(words).
    """
    words_str = "".join(words)
    length = len(words_str)
    i = 0
    while i + length < len(sentence):
        substring = sentence[i: i + length]
        if is_words_in_substring(words, substring):
            return i, substring
        i += 1
    return -1, "Not found"

def is_words_in_substring(words, substring):
    for word in words:
        if word not in substring:
            return False
    return True
if __name__ == "__main__":
    words = ["can", "apl", "ana"]
    sentence = "amanaplanacanal"
    index, substring = find_all_substrings(words, sentence)
    print("index: ", index)
    print("substring: ", substring)

    words = ["can", "apl", "ana"]
    sentence = "amanaplanacaanaaplcanl"
    index, substring = find_all_substrings(words, sentence)
    print("index: ", index)
    print("substring: ", substring)

