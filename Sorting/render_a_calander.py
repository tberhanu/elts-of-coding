# start Question
from collections import namedtuple

Event = namedtuple('Event', ('start', 'end'))
Point = namedtuple('Point', ('time', 'is_starting_point'))

def find_max_simultaneous_events(A):
    """
    Suppose each day consists of a number of events, where an event is specified as a start time and end time.
    Write a program that takes a set of events, and determines the maximum number of events that take place
    concurrently (Having some intersection time slot in common).

    Strategy:
        1. Brute-force: Double for loop: For each pair of (start, end), check how many other (start, end) overlap,
                        and return the maximum overlap you come across. Since we've N Events to loop through and each
                        Event has 2 end points, O(2*N), and then checking the number of other events that overlap takes
                        O(N), so O(2*N*N) which is O(N * N).

        2. Let's SORT EVERYTHING !!! Let's sort everything in the POINT level regardless whether a START or END point,
           then we may have a COUNTER to increment when touching STARTING POINT, and decrement when touching ENDING
           POINT, while saving the MAXIMUM we've come across and return it at last.
           This make as sense as when a session start, we have 1 session, and if another session also start, we'll
           have 2 sessions, but if we reached the end of one of the started session, then we go back to 1 session and
           goes on until the end.
           Challenges: While SORTING, what if we have SAME POINT for two points, one with the START label, and
                       another one with the END label? Should we first increment or decrement?
           Answer: Better to consider the one with the START label first to increment, and then decrement. But if same
                   point happen for those with the same label, then we break tie arbitrarily(=choosing randomly).

           Time Complexity: O(N log N) for Sorting, and O(N) looping through the array, so overall: O(N log N)
           Space Complexity: O(E) where E is the size of the Endpoint Array we create to collect all POINTS.
    """
    start_points = [Point(event.start, True) for event in A]
    end_points = [Point(event.end, False) for event in A]
    points = start_points + end_points
    # The following KEY inside SORT doesn't alter the data, rather it's just to set the rule of sorting
    points.sort(key=lambda point: (point.time, not point.is_starting_point)) # bc False comes before True in sorting

    print(points)

    counter = 0
    max_counter = 0
    for p in points:
        if p.is_starting_point:
            counter += 1
            max_counter = max(max_counter, counter)
        else:
            counter -= 1

    return max_counter





if __name__ == "__main__":
    e1 = Event(start=1, end=5)
    e2 = Event(start=2, end=7)
    e3 = Event(4, 5)
    e4 = Event(6, 10)
    e5 = Event(8, 9)
    e6 = Event(9, 17)
    e7 = Event(11, 13)
    e8 = Event(12, 15)
    e9 = Event(14, 15)
    e10 = Event(12, 17)

    A = [e4, e3, e1, e2, e8, e7, e5, e6, e9, e10]
    result = find_max_simultaneous_events(A)
    print(result)
