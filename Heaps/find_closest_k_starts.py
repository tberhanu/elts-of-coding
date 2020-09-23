import heapq
class Star:
    def __init__(self, x, y, z, name=""):
        self.x = x
        self.y = y
        self.z = z
        self.name = name

    def distance(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

def find_closest_k_stars(k, stars):
    """
    Question: Consider a coordinate system for the Milky Way in which Warth is at (0, 0, 0). The
              Milky Way consists of approximately 10**12 stars, adn their coordinates are stored in a file.
              How would you compute the k stars which are closest to Earth?
    Answer: Brute-force is putting all starts into an array (if RAM is not a limitation), and do the normal
            sorting, O(N log N).
            Smart approach: is populating the first K stars inside our maxHeap, and after that keep poping
                            out the furthest(max) one before pushing the next start. Once you go through
                            all the stars, you will remain a maxHeap with K of the closes stars to the
                            Earth which you can easily retrieve in order via heapq.nlargest(k, maxHeap).

    Time Complexity: O(N log K) as maxHeap takes O(log K) & also touching each star, O(N)
    Space Complexity: O(K) for our maxHeap
    """
    maxHeap = []
    # reader = csv.reader(stars)
    reader = stars # Assuming stars is a list of lists for the sake of simplicity
    for line in reader:
        star = Star(line[0], line[1], line[2], line[3])
        heapq.heappush(maxHeap, (-star.distance(), star)) # need to take the NEGATIVE to use maxHeap
        if len(maxHeap) == k + 1:
            heapq.heappop(maxHeap)

    result = [(s[1].name, -s[0]) for s in heapq.nlargest(k, maxHeap)]
    return result

if __name__ == "__main__":
    k = 3
    stars = [(12, 23, 12, "a"), (9, 0, 0, "b"), (0, 1, 1, "c"), (99, 99, 99, "e"), (23, 24, 25, "f")]
    result = find_closest_k_stars(k, stars)
    print(result)