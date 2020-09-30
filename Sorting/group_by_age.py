from collections import namedtuple, Counter
import random
import string
Person = namedtuple("Person", ("age", "name"))
def group_by_age(people):
    """
    brute-force: We can SORT each person by their AGE and done, which takes O(N log N).
                people.sort(key=lambda person: person.age)
    Counting Search: Using Hashtable which may take O(N)
                    Time: O(N)
                    Space: O(N)
                    Refer page 196 for Space: O(1) and Time O(N)
    """
    ages = [p.age for p in people]
    counter = Counter(ages)
    print(counter)
    result = []
    for k, v in counter.items():
        for i in range(v):
            result.append(k)

    return result


if __name__ == "__main__":
    people = []
    for i in range(6):
        age = random.randint(18, 20)
        name = random.choice(string.ascii_letters)
        person = Person(age, name)
        people.append(person)

    print(people)
    print("++++++++++++++++")
    result = group_by_age(people)
    print(result)
