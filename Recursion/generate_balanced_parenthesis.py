# Star Question
"""
Write a program that takes as input a number and returns all the strings with that number of matched pairs of parens.
For ex. the set of strings containing two pairs of matched parens is {(()), ()()}, and those with three pairs will be
{((())), (()()), (())(), ()(()), ()()()}.
Strategy:
    1. Start with number of OPEN and CLOSE parenthesis both equals to N.
    2. If number of OPEN >= CLOSE, take one OPEN, "(", and call recursive function for the rest by deducting OPEN by 1.
    3. If number of OPEN == 0 while still CLOSE > 0, then can't proceed ahead except dumping the rest of CLOSE
       parenthesis at the tail of the RESULT. To do so, call recursive function with CLOSE to be ZERO.
    4. If reaching both OPEN and CLOSE to ZERO, then append the RESULT to the COLLECTOR.
"""

def generate_balanced_parenthesis_driver(N):
    result = ""
    open = N
    close = N
    collector = []
    return generate_balanced_parenthesis(open, close, result, collector)

def generate_balanced_parenthesis(open, close, result, collector):
    if open == 0 and close == 0:
        collector.append(result)
    elif open >= close:
        generate_balanced_parenthesis(open - 1, close, result + "(", collector)
    elif open == 0:
        closings = ")" * close
        generate_balanced_parenthesis(0, 0, result + closings, collector)
    else:
        generate_balanced_parenthesis(open - 1, close, result + "(", collector)
        generate_balanced_parenthesis(open, close - 1, result + ")", collector)

    return collector

if __name__ == "__main__":
    result = generate_balanced_parenthesis_driver(3)
    print(result)
    result = generate_balanced_parenthesis_driver(4)
    print(result)