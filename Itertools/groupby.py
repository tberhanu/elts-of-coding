import itertools
from Itertools import people
if __name__ == "__main__":
    def get_state(person):
        return person['state'] # telling we want to groupt by 'state'

    person_group = itertools.groupby(people, get_state)
    for key, group in person_group:
        print(key)
        for person in group:
            print(person)
        print()
    print("how many person in each group: ")
    person_group = itertools.groupby(people, get_state)
    for key, group in person_group:
        print(key, len(list(group)))

