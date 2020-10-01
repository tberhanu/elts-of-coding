def find_closest_entries_in_three_sorted_arrays(sorted_arrays):
    """
    Tess Strategy:
        Time: O(N) w/r N is the maximum array length of the three arrays

    Page 211 uses bintrees.RBTree(), check it out.
    """
    a, b, c = sorted_arrays[0], sorted_arrays[1], sorted_arrays[2]
    smallest_gap = float("inf")
    collector = []
    while a and b and c:
        diff = sum([abs(a[0] - b[0]), abs(a[0] - c[0]), abs(b[0] - c[0])])
        if diff < smallest_gap:
            smallest_gap = diff
            collector = []
            collector.append([a[0], b[0], c[0]])
        if diff == smallest_gap:
            collector.append([a[0], b[0], c[0]])
        e = min(a[0], b[0], c[0])
        if e in a:
            a.remove(e)
        elif e in b:
            b.remove(e)
        else:
            c.remove(e)

    return collector


if __name__ == "__main__":
    sorted_arrays = [[5, 10, 15], [3, 6, 9, 12, 15], [8, 16, 24]]
    result = find_closest_entries_in_three_sorted_arrays(sorted_arrays)
    print(result) # 15, 15, 16

    sorted_arrays = [[5, 10, 15, 20], [3, 6, 9, 12, 15, 16], [8, 15, 16, 24]]
    result = find_closest_entries_in_three_sorted_arrays(sorted_arrays)
    print(result)  # 15, 15, 15

    sorted_arrays = [[5, 10, 15, 20], [3, 6, 9, 12, 15], [6, 8, 16, 24]]
    result = find_closest_entries_in_three_sorted_arrays(sorted_arrays)
    print(result)  # 15, 15, 16
