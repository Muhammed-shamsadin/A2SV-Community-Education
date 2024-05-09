class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # [3, 2, (4), 1]      k = []
        # [4, 2, 3, 1]        k = [3, ]
        # [1, 3, 2,| 4]       k = [3, 4]
        # [3, 1, 2,| 4]       k = [3, 4, 2]
        # [2, 1,| 3, 4]       k = [3, 4, 2, 3] 
        # [2, 1,| 3, 4]       k = [3, 4, 2, 3, 1]
        # [1, |2, 3, 4]       k = [3, 4, 2, 3, 1, 2]
        # [1, |2, 3, 4]       k = [3, 4, 2, 3, 1, 2, 1]
        # [|1, 2, 3, 4]       k = [3, 4, 2, 3, 1, 2, 1, 1]

        n = len(arr)
        k = []

        for i in range(n):
            maxim = max(arr[:n - i])
            maxim_indx = arr.index(maxim) + 1
            arr[:maxim_indx] = reversed(arr[:maxim_indx])
            k.append(maxim_indx)

            arr[:n - i] = reversed(arr[:n - i])
            k.append(n - i)

        return k
