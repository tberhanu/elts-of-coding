MPG = 20 # MPG is Mile Per Gallon
from collections import namedtuple
def find_ample_city_from_book(gallons, distances):
    """
    gallons[i] is the amount of gas in city i, and distances[i] is the distance city i to the next city.
    Conceptual Strategy:

    """
    remaining_gallons = 0
    CityAndRemainingGas = namedtuple('CityAndRemainingGas', ('city_index', 'remaining_gallons'))
    city_remaining_gallons_pair = CityAndRemainingGas(0, 0)
    num_cities = len(gallons)
    for i in range(1, num_cities):
        remaining_gallons += gallons[i - 1] - (distances[i - 1] // MPG)
        if remaining_gallons < city_remaining_gallons_pair.remaining_gallons:
            city_remaining_gallons_pair = CityAndRemainingGas(i, remaining_gallons)

    return city_remaining_gallons_pair.city_index

def find_ample_city_tess_improving_book(gallons, distances):
    ample_city = None
    left_over_gallons = 0
    for i in range(len(gallons)):
        diff_gallons = gallons[i] - (distances[i] // MPG)
        net_gallons = left_over_gallons + diff_gallons
        if ample_city is None:
            if diff_gallons >= 0:
                ample_city = f"city at index: {i}"
                left_over_gallons = net_gallons

        else:
            if net_gallons < 0:
                ample_city = None
                left_over_gallons = 0
    return ample_city

def find_ample_city(stations):
    """
    A number of cities are arranged on a circular road. You need to visit all the cities and come back to the starting
    city. A certain amount of gas is available at each city. The amount of gas summed up over all cities is equal to the
    amount of gas required to go around the road once. Your gas tank has unlimited capacity. Call a city AMPLE if you
    can begin at that city with an empty task, refill at it, then travel through all the remaining cities, refilling at
    each, and return to the AMPLE city, without running out of gas at any point.

    Question: Given an instance of the gasup problem, how would you efficiently compute an ample city? You can assume
              that there exists an ample city.
    Time: O(N) As a couple of rotation is expected
    Space: O(1)
    """
    leftover_miles = 0
    ample_city = None
    count = 0
    i = 0
    while True:
        doable_miles = leftover_miles + stations[i].gallon * MPG
        if doable_miles >= stations[i].distance:
            if ample_city == stations[i].name:
                return ample_city
            leftover_miles = doable_miles - stations[i].distance
            if ample_city is None:
                ample_city = stations[i]
                count = 0
            else:
                count += 1
                if count == len(stations):
                    return ample_city
        else:
            ample_city = None
            leftover_miles = 0

        i = (i + 1) % len(stations)

    return ample_city

class GasStation:
    def __init__(self, station_name, gallon, mile, next_station):
        self.name = station_name
        self.gallon = gallon
        self.distance = mile
        self.next_station = next_station

if __name__ == "__main__":
    print("________ by Tess ________")
    G = GasStation("G", 10, 100, "A")
    F = GasStation("F", 10, 200, "G")
    E = GasStation("E", 25, 600, "F")
    D = GasStation("D", 30, 400, "E")
    C = GasStation("C", 5, 200, "D")
    B = GasStation("B", 20, 600, "C")
    A = GasStation("A", 50, 900, "B")
    stations = [A, B, C, D, E, F, G]
    ample_city = find_ample_city(stations)
    print("Ample City Name: ", ample_city.name)
    print("Ample City Gallon: ", ample_city.gallon)
    print("Ample City Distance: ", ample_city.distance)
    print("________ by book ___________")
    gallons = [50, 20, 5, 30, 25, 10, 10]
    distances = [900, 600, 200, 400, 600, 200, 100]
    city_index = find_ample_city_from_book(gallons, distances)
    print("city index: ", city_index)
    print("city gallon: ", gallons[city_index])
    print("city distande: ", distances[city_index])
    print("_____ improved ______")
    ample_city = find_ample_city_tess_improving_book(gallons, distances)
    print(ample_city)
