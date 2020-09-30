# Star Question
from collections import namedtuple
Interval = namedtuple('Interval', ('start', 'end'))
def add_interval(disjoint_intervals, new_interval):
    """
    Suppose the time during the day that a person is busy is stored as a set of disjoint time intervals. If an event
    is added to the person's calendar, the set of busy times may need to be updated.
    For example, if the initial set of intervals is [-4, 1], [0, 2], [3, 6], [7, 9]. [11, 12], [14, 17], and
    the added interval is [1, 8], the result is [-4, -1], [0, 9], [11, 12], [14, 17].

    Question:
    Write a program which takes as input an array of disjoint closed intervals with integer endpoints, sorted
    by increasing order of left endpoint, and an interval to be added, and returns the union of the intervals in the
    array and the added interval. Your result should be expressed as a union of disjoint intervals sorted by left
    endpoint.
    """
    lefty_intervals = []
    i = 0
    # if the new_interval start is greater than disjoint_intervals end, then obviously no overlap so continue, so
    # save them as lefty_intervals.
    while (i < len(disjoint_intervals) and new_interval.start > disjoint_intervals[i].end):
        lefty_intervals.append(disjoint_intervals[i])
        i += 1

    # Once the new interval start is less than one of the intervals end, we need more investigation to perform as
    # there is a chance for being overlapped or disjointed. If disjoint start is greater than the interval end, then
    # they are disjoint, so place the new_interval after the lefty_intervals followed by the rest of disjoint_intervals.
    # But, if disjoint start is to the LEFT of the interval end, then overlap happen so let's UNIONIZE them and keep
    # rolling the loop until we found another interval separated(=disjointed) from the rolling UNIONS.
    while (i < len(disjoint_intervals) and new_interval.end >= disjoint_intervals[i].start):
        union_interval = Interval((min(disjoint_intervals[i].start, new_interval.start)),
                                  (max(disjoint_intervals[i].end, new_interval.end)))
        new_interval = union_interval
        i += 1

    # Let's concatenate the three disjointed intervals. Remember, either the lefty_intervals or the
    # disjointed_intervals have a chance to be Empty Array. Remember ARRAY SLICING doesn't throw IndexOutOfBound
    # error, even though array[len(array):], rather returns Empty Array, [].
    return lefty_intervals + [new_interval] + disjoint_intervals[i:]

# def does_intersect(interval, next_interval):
#     """
#     This snippet code works fine, enen though we don't need this for this problem.
#     """
#     Point = namedtuple("Point", ("x", "label"))
#     point1, point2 = Point(interval.start, "a"), Point(interval.end, "b")
#     point3, point4 = Point(next_interval.start, "a"), Point(next_interval.end, "b")
#     points = [point1, point2, point3, point4]
#     points.sort(key=lambda point: (point.x, point.label))
#     prev = "c"
#     for point in points:
#         if point.label == prev:
#             return True # Intersect
#         else:
#             prev = point.label
#     return False


if __name__ == "__main__":
    # a = Interval(0, 9)
    # b = Interval(9, 18)
    # print(does_intersect(a, b))
    arrays = [[-4, -1], [0, 2], [3, 6], [7, 9], [11, 12], [14, 17]]
    disjoint_intervals = []
    for array in arrays:
        interval = Interval(start=array[0], end=array[1])
        disjoint_intervals.append(interval)
    new_interval = Interval(1, 8)

    result = add_interval(disjoint_intervals, new_interval)
    print(result)