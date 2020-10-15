def optimum_task_assignment(task_durations):
    """
    Consider assigning tasks to workers where each worker must be assigned exactly TWO TASKS, and each task has a
    fixed amount of time it takes.
    Design an algorithm that takes as input a set of tasks and returns an optimum assignment.

    Note: Simply enumerating all possible sets of pairs of tasks is not feasible, takes too much, N!/(2 ** N/2)
          so better to use Greedy Algorithm.

    Strategy:
        Order the tasks and assign the one with smallest time and the one with the largest time to one worker, and
        continue doing that. Ex. [1, 2, 4, 4, 5, 6] >> (1, 6), (2, 5), and (4, 4)
    """
    from collections import namedtuple
    PairedTasks = namedtuple('PairedTasks', ('small_task', 'large_task'))
    task_durations.sort()
    result = [PairedTasks(task_durations[i], task_durations[~i]) for i in range(len(task_durations) // 2)]
    return result

if __name__ == "__main__":
    task_durations = [5, 2, 1, 6, 4, 4]
    result = optimum_task_assignment(task_durations)
    print(result)