# Hard
"""
Page 263
Consider the problem of laying out text using a fixed width font. Each line can hold no more than a fixed number of
characters. Words on a line are to be separated by exactly one blank. Therefore, we may be left with whitespace at the
end of a line(since the next word will not fit in the remaining space). This whitespace is visually unappealing.
Define the messiness of the end-of-line whitespace as follows. The messiness of a single line ending with B blank
characters is B ** 2. The total messiness of a sequence of lines is the sum of the messinesses of all the lines. A
sequence of words can be split across lines in different ways with different messiness.
Given text, i.e. a string of words separated by single blanks, decompose the text into lines such that no word is split
across lines and the messiness of the decomposition is minimized. Each line can hold no more than a specified number
of characters.

Hint: Focus on the last word and the last line.

"""
def minimum_messiness(words, line_length):
    lines = [[] for _ in range(len(words))]
    lines[0] = [words[0]]
    print(lines)
    num_remaining_blanks = line_length - len(words[0])
    min_messiness = ([num_remaining_blanks ** 2] + [float('inf')] * (len(words) - 1))
    print(min_messiness)



    for i in range(1, len(words)):
        num_remaining_blanks = line_length - len(words[i])
        min_messiness[i] = min_messiness[i - 1] + num_remaining_blanks ** 2
        for j in reversed(range(i)):
            num_remaining_blanks = num_remaining_blanks - (len(words[j]) + 1)
            if num_remaining_blanks < 0:
                break
            if j - 1 < 0:
                prev_prev_messiness = 0
            else:
                prev_prev_messiness = min_messiness[j - 1]

            current_line_messiness = num_remaining_blanks ** 2

            if min_messiness[i] > prev_prev_messiness + current_line_messiness:
                min_messiness[i] = prev_prev_messiness + current_line_messiness
                lines[i] = words[j: i+1]

    print("lines: ", lines)
    best_lines = []
    i = len(lines) - 1
    while i >= 0:
        if not lines[i]:
            i -= 1
            continue
        best_lines.append(lines[i])
        if i - 1 >= 0 and lines[i][0] == lines[i - 1][-1]:
            i -= 2
        else:
            i -= 1

    answer = [" ".join(e) for e in best_lines[::-1]]
    print(answer)
    print("b: ", best_lines)
    return min_messiness[-1]



if __name__ == "__main__":
    # words = ["Tushar", "Roy", "likes", "to", "code"]
    # line_length = 10
    # m_m = minimum_messiness(words, line_length)
    # print(m_m)

    words = ["aaa", "bbb", "c", "d", "ee", "ff", "ggggggg"]
    mm = minimum_messiness(words, 10)
    print(mm)

