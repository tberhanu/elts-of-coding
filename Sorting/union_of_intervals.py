# Star Question
from collections import namedtuple
"""
Consider sets of intervals with integer endpoints; the intervals may be open or closed at either end. We want to 
compute the union of the intervals in such sets. 
Example:
    Input: pts = [ (0, 3), [1, 1], [2, 4], [3, 4),         
                   [5, 7), [7, 8), [8, 11), (9, 11],      
                   (13, 15), (12, 16], [12, 14], (16, 17]
                 ]
    Output:
            unions = [(0, 4], [5, 11], [12, 17)]
    
    
     Time: O(N log N) as we Sort, and also just loop over N after that.
     Detail: Page 194
"""
Point = namedtuple("Point", ("value", "is_closed"))
class Interval:

    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __lt__(self, other):
        if self.left.value != other.left.value:
            return self.left.value < other.left.value
        elif self.left.is_closed and not other.left.is_closed:
            return True
        else:
            return False


    def __str__(self):
        a, b = "(", ")"
        if self.left.is_closed:
            a = "["
        if self.right.is_closed:
            b = "]"
        return f"{a}{self.left.value}, {self.right.value}{b}"



def union_of_intervals(intervals):
    intervals.sort()
    result = [intervals[0]]
    for interval in intervals[1:]:
        prev = result[-1]
        if ((interval.left.value < prev.right.value) or
            (interval.left.value == prev.right.value and (interval.left.is_closed or prev.left.is_closed))):
            if ((interval.right.value > prev.right.value) or
                (interval.right.value == prev.right.value and (interval.right.is_closed or prev.right.is_closed))):
                # Bug I found from the BOOK
                if (interval.right.value == prev.right.value  and (interval.right.is_closed or prev.right.is_closed)):
                    if not prev.right.is_closed:
                        prev.right = interval.right
                else:
                    prev.right = interval.right

        else:
            result.append(interval)

    return result

if __name__ == "__main__":
    pts = [(0, "o", 3, "o"), (1, "c", 1, "c"), (2, "c", 4, "c"), (3, "c", 4, "o"),
           (5, "c", 7, "o"), (7, "c", 8, "o"), (8, "c", 11, "o"), (9, "o", 11, "c"),
           (13, "o", 15, "o"), (12, "o", 16, "c"), (12, "c", 14, "c"), (16, "o", 17, "o")]
    intervals = []
    for pt in pts:
        left = Point(pt[0], pt[1] == "c")
        right = Point(pt[2], pt[3] == "c")
        interval = Interval(left, right)
        intervals.append(interval)

    intervals.sort()
    for interval in intervals:
        print(interval.left, interval.right)
    print("++++++++++++++++++++")
    results = union_of_intervals(intervals)
    for result in results:
        print(result)