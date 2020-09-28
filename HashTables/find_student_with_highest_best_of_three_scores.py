from collections import defaultdict
import heapq
def find_student_with_highest_best_of_three_scores(name_score_data):
    """
    Question: Write a program which takes as input a file containing test scores an returns the student
              who has the maximum score averaged across his or her top three tests. If the student
            has fewer than three test score ignore that student.

    Brute-force: O(N log N): We can iterate through the data, SORT the scores, and average out the three highest scores.
    Smart Solution: O(N): Using minHeap and Hashtable, default dictionary.
                          1. Create a default dictionary with sid as key, and default value is Empty List.
                          2. Loop through the data, and save each sid as key, and PUSH to the List as a minHeap.
                          3. So, heappush until having 3 scores, and after that use heappushpop which will push
                             the new score, and pop out the most minimum one so that we remain with 3 top scores.
                          4. Use list comprehension to retrieve the maximum score.
    """
    ddict = defaultdict(list)
    for data in datas:
        sid, scores = data.split(":")
        scores = scores.split(",")
        for score in scores:
            lst = ddict[sid]
            if len(lst) < 3:
                heapq.heappush(lst, int(score))
            else:
                heapq.heappushpop(lst, int(score))

    max_score = max(sum(datas) for sid, datas in ddict.items() if len(datas) == 3)

    return max_score



if __name__ == "__main__":
    datas = ["001:1,2,2,3", "002:8,2,0", "003:9,1,1,0,5", "004:100,99, 0"]
    top_scorer = find_student_with_highest_best_of_three_scores(datas)
    print(top_scorer)