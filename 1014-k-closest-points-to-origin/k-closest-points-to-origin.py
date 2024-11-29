class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []

        for i, point in enumerate(points):
            x, y = point
            distance = math.sqrt(x**2 + y**2)
            distances.append((distance, i))
        distances.sort()
        result = []

        for distance, i in distances[:k]:
            result.append(points[i])
        return result