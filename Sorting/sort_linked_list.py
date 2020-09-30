def sort_linked_list(ll):
    """
        Strategy:
            1. Loop through the linked list and append each Node to the ARRAY, O(N), since looping through N
               number of Nodes, and APPENDING to Array takes only O(1), unlike INSERTING w/c takes O(N).
            2. Sort the array in REVERSE OREDER i.e. array.sort(reverse=True) w/c takes O(N log N)
            3. Add each NODE from the Array to the Linked List, O(N), as adding more Node to Linked List takes O(1)

            Therefore, overall Time: O(N log N), and Space: O(N)

            Page 198 got solutions:
                Solution 1. Time: O(N * N) and Space: (N)
                Solution 2. Time: O(N * N) and Space: (1)
                Solution 3. Time: O(N log N) and Space: O(log N) using Merge Sort Concept.

                Check them out !!!!
    """
    pass