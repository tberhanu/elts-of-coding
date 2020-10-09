# Hard
"""
Page 263
Consider the problem of laying out text using a fixed width font. Each line can hold no more than a fixed number of
characters. Words on a line are to be separated by exactly one blank. Therefore, we may be left with whitespace at the
end of a line(since the next word will not fit in the remaining space). This whitespace is visually unappealing.
Define the messiness of the end-of-line whitespace as follows. The messiness of a single line ending with B blank
characters is B ** 2. The toatal messiness of a sequence of lines is the sum of the messinesses of all the lines. A
sequence of words can be split across lines in different ways with different messiness.
Given text, i.e. a string of words separated by single blanks, decompose the text into lines such that no word is split
across lines and the messiness of the decomposition is minimized. Each line can hold no more than a specified number
of characters.

Hint: Focus on the last word and the last line.

"""
def minimum_messiness(words, line_length):
    pass

