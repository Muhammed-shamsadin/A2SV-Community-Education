class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n, m = len(firstList), len(secondList)
        ptr_first = ptr_second = 0
        res = []

        while ptr_first < n and ptr_second < m:
            # Get the start and end of both intervals
            start1, end1 = firstList[ptr_first]
            start2, end2 = secondList[ptr_second]

            # Check if the intervals overlap
            if end1 >= start2 and end2 >= start1:
                # Add the intersection to the result list
                res.append([max(start1, start2), min(end1, end2)])

            # Move to the next interval in the list that ends earlier
            if end1 < end2:
                ptr_first += 1
            else:
                ptr_second += 1

        return res
