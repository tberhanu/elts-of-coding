# Star Dynamic Programming Quesion
def min_edit_to_transform_strings(str1, str2):
    """
    Question: Write a program that takes two strings and computes the minimum number of edits needed to transform
              the one string into the other string whichever require the minimum number of edits. A single EDIT is
              defined as a single INSERTION, or DELETION, or SUBSTITUTION of a single character.
              Example: str1 = "Saturday" and str2 = "Sunday"
    Strategy: DP
        1. Get a matrix table of size (N + 1) by (M + 1) w/r N and M are length of the str1 and str2.
        2. Fill the matrix first ROW from 0 upto N, and first COLUMN from 0 upto M.
        3. Each filled BOX at (i, j) tells that str1 from 0 to i takes a minimum steps of matrix[i][j] to transform
           to str2 from 0 to j and vice versa. Therefore, the already filled boxes at the front row and col gives
           correct meaning according to this explanation.
        4. Each step forward, matrix[i][j], the letter that corresponds to str1[i] and str2[j] are the same, then we
           can assume the shortest number of edits needed is same as that of matrix[i-1][j-1].
        5. But, if str1[i] is d/t from str2[j], then we need to take the MINIMUM path upto the box just at the TOP, or
           at the LEFT or at the top-left-corner, and add ONE MORE STEP on it.

    Time: O(N * M)
    Space: O(N * M) as we used the Matrix Table (N+1) by (M+1)
    """
    matrix = create_the_matrix(str1, str2)
    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if str1[i] == str2[j]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                a = matrix[i-1][j-1]
                b = matrix[i-1][j]
                c = matrix[i][j-1]
                val = min(a, b, c) + 1
                matrix[i][j] = val


    return matrix[len(str1) - 1][len(str2) - 1]

def create_the_matrix(str1, str2):
    str1 = " " + str1
    str2 = " " + str2
    matrix = [[None for _ in range(len(str2))] for _ in range(len(str1))]
    matrix[0] = [i for i in range(len(str2))]
    for i in range(len(str1)):
        matrix[i][0] = i
    return matrix

if __name__ == "__main__":
    str1 = "saturday"
    str2 = "sundays"
    result1 = min_edit_to_transform_strings(str1, str2)
    result2 = min_edit_to_transform_strings(str2, str1)
    print(result1) # 4
    print(result2) # 4

    print("+++++++++++++++++")

    str1 = "abcdef"
    str2 = "azced"
    result1 = min_edit_to_transform_strings(str1, str2)
    result2 = min_edit_to_transform_strings(str2, str1)
    print(result1) # 3
    print(result2) # 3



