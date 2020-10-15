"""
Application Queries ust be processed by the database one at a time, but can be done in any order. The time query waits
before its turn comes is called its WAITING TIME, so NOTE that it's the time ONLY UNTIL the START of the LAST JOB b/c
nothing to be waited once the last job started to be processed.
Ex. i) [2, 5, 1, 3]: 2 has 0 WT, 5 has 2 WT, 1 has 2 + 5 = 7 WT, and 3 has 2 + 5 + 1 = 8 WT >>> 0+2+7+8= 17 total WT
    then 2 waiting time for 3 queries, then 5 waiting time for 2 queries,
                  and 1 waiting time for 1 query.
    so, 2*3 + 5*2 + 1*1 = 17 total waiting time

    ii) [1, 2, 3, 5]: 1 has 0 waiting time, 2 has 1 WT, 3 has 1 + 2 = 3 WT, 5 has 1 + 2 + 3 WT
                       >> 0 + (1) + (1 + 2) + (1 + 2 + 3) = 10 total WT.
                    In other words, this can be written like this:
                        1*3(=1 WT for 3 queries) + 2*2(=2 WT for 2 queries) + 3*1(=3 WT for 1 query) = 10 total WT

    So, better to finish the small tasks first since the process time of each query adds to the waiting time of all
    queries remaining to be processed.

    Time: O(N log N) for sorting the service_times.
    Space: O(1)
    Note: Solving this problem by enumerating all schedules and picking the best one takes O(N!) so better to use
          Greedy Algorithm.
"""
def minimun_total_waiting_time(service_times):
    service_times.sort()
    total_waiting_time = 0
    for i, time in enumerate(service_times):
        other_queries = len(service_times) - (i + 1)
        # the last largest wait time query won't be included as it multiplied by other_queries w/c will be 0.
        total_waiting_time += time * other_queries

    return total_waiting_time

if __name__ == "__main__":
    service_times = [2, 5, 3, 1]
    result = minimun_total_waiting_time(service_times)
    print(result)
