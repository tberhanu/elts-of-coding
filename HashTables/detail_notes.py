"""
Hash tables:
    *** FOR ANY PROBLEM, HAVE A HASH TALBE TO SOLVE THE PROBLEM !!!!!!!!!!!!!!!!!! ***

    Time Complexties:
        Lookup, Insert, Delete: O(1)
        Insertion: O(1) for a good hash function, but O(N) in worst case scenario which is very rare
        Iteration: .items() for key-value pairs
                   .keys() for keys
                   .values() for values
        Not every type is "hashable", as MUTABLE containers are not hashable.
        Built in hash() function >> __hash(self)__

        Hash table based Data Structures:
            1. set:
                s = set()
                s.add(42), s.remove(42), s.discard(123)
                elt in s
                set1 <= set2 >> set1 is subset of set2
                set1 - set2 >> elts in set1 that are not in set2

            2. dict: throws KeyError exception if key not found

            3. collections.defaultdict:
                d = collections.defaultdict(list)
                return [] if key not found in d, unlike the normal dict.
            4. collectioins.OrderedDict:
                Preserves the ORDER in which the keys are inserted, unlike the normal dict.
                od = collections.OrderedDict()
                od["a"] = 1
                od["b"] = 2
                popitem(last=True): The popitem() method for ordered dictionaries returns and
                                    removes a (key, value) pair. The pairs are returned in
                                    LIFO order if last is True or FIFO order if False.
            5. collections.Counter: used for counting number of occurrences of keys
                c = collections.Counter(a=3, b=1)
                d = collections.Counter(a=1, b=2)
                c + d >> {'a': 4, 'b': 3}
                c - d >> {'a': 2} # it keeps only POSITIVE COUNTS
                c & d >> {'a': 1, 'b': 1} # INTERSECTION, takes min(c, d)
                c | d >> {'a': 3, 'b': 2} # UNION, takes max(c, d)



"""
import collections
def counter_usage():
    s = "hello world!"
    c = collections.Counter(s)
    print(c)
    arr = ["a", "b", "a", "c", "a", "a", "b", "d"]
    c = collections.Counter(arr)
    print(c)

def can_str_be_palindrome(s):
    """
    Question: Given a string, check if you can derive a palindrome out of it by rearranging.
    input: "edified"
    output: True because "deified" is a palindrome

    Solution: Each character COUNT should be EVEN, and only at most ONE character is allowed to be ODD COUNT.

    Time Complexity: O(N) where N is the length of string
    Space Complexity: O(C) where C is the number of DISTINCT characters inside the string
    """
    c = collections.Counter(s)
    result = sum(1 for e in c.values() if e % 2 != 0)
    return result <= 1

if __name__ == "__main__":

    counter_usage()
    r = can_str_be_palindrome("edified")
    print(r) # True
    r = can_str_be_palindrome("edifiedd")
    print(r) # False
    r = can_str_be_palindrome("edifieddd")
    print(r) # True

