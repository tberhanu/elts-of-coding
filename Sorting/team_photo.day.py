from collections import namedtuple
Player = namedtuple('Player', 'height')
class Team:
    def __init__(self, heights):
        self.heights = [Player(h) for h in heights]

def does_valid_placement_exitsts(back_team, front_team):
    """
    You are taking pictures of pairs of opposing teams, all teams have teh same number of players. A team photo
    consists of a front row of players and back row of players. A player just at the back of another team player
    must be taller than the player in front of him. All players in a row must be from the same team.
    Given two teams adn their heights, check if it is possible to place players to take the photo subject to the
    placement constraint.

    Strategy:
        Not sure how to proceed? Always, SORT SOMETHING, and try to see ANY PATTERN. YES, for each of the TALLEST
        player from the front team, there should be another More TALLEST from the back team; otherwise DONE, not
        possible. If we've the TALLEST from the back team, CONTINUE asking the same question for the SECOND
        TALLEST player, and if can't get another TALLEST to 'counter-attack', then DONE. If all the front 'tallest'
        have a corresponding 'tallest' from the back team, then YES, it's POSSIBLE!!!

        Time: O(N log N) where N is number of all players as we SORT them, and ofcourse we loop over them.
    """
    return all(back > front for back, front in zip(sorted(back_team.heights), sorted(front_team.heights)))


if __name__ == "__main__":
    height_a = [2, 6, 3, 7, 8, 9, 6]
    height_b = [4, 5, 6, 2, 3, 1, 2]
    back_team = Team(height_a)
    front_team = Team(height_b)
    result = does_valid_placement_exitsts(back_team, front_team)
    print(result) # True
    height_a = [2, 6, 3, 7, 8, 9, 6]
    height_b = [4, 5, 6, 2, 3, 2, 2]
    back_team = Team(height_a)
    front_team = Team(height_b)
    result = does_valid_placement_exitsts(back_team, front_team)
    print(result) # False