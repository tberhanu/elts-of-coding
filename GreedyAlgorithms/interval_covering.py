from collections import namedtuple
def find_minimum_visits(intervals):
    """
    Consider a foreman responsible for a number of tasks on the factory floor. Each task starts at a fixed time and ends
    at a fixed time. Ther forman wants to visit the floor to check on the tasks. Your job is to help him minimize the
    number of visits he makes.
    Question: You are given a set of CLOSED INTERVALS. Design an efficient algorithm for finding the minimum sized set
              of numbers theat covers all the intervals.
              Example:  Input: [0, 3], [2, 6], [3, 4], [6, 9]
                        Output: [3, 6] i.e. Visiting at time 3 and 6 is enough to supervise all the tasks/intervals.

    Strategy:
        Enumerating every possible subset of endpoints may take too much as there are (2 ** K) subsets for k size set.
        So, let's use Greedy Algorithm.
        1. Sort the intervals by their END POINT.
        2. Take the first minimum END POINT, and traverse through others.
        3. If that end point is found in other intevals just keep going, until you found an inteval not including that
           end point in which case you need to save such inteval's END POINT, AND continue traversing same way but this
           time using the newly END POINT.

    Time: O(N log N)
    Space: O(k) where k is the number of disjoint intervals
    """
    intervals.sort(key=lambda interval: interval.end)
    visits = [intervals[0].end]
    for interval in intervals[1:]:
        if interval.start <= visits[-1] <= interval.end:
            continue
        else:
            visits.append(interval.end)
    return visits

if __name__ == "__main__":
    Iterval = namedtuple('Iterval', ('start', 'end'))
    a, b, c, d = Iterval(0, 3), Iterval(2, 6), Iterval(3, 4), Iterval(6, 9)
    intervals = [a, b, c, d]
    result = find_minimum_visits(intervals)
    print(result)

    a, b, c, d = Iterval(1, 2), Iterval(2, 3), Iterval(3, 4), Iterval(4, 5)
    intervals = [a, b, c, b, c, d]
    result = find_minimum_visits(intervals)
    print(result)


