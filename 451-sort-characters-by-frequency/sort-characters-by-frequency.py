class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        Approach: first hold the numbers of the frequency ..and then we will sort alphabetically.
        '''
        # l = [i for i in s]
        # l = sorted(l,key=lambda x: l.count(x))
        # print(l)
        # l.reverse()
        # return "".join(l)

        counter = Counter(s)
        bucket = defaultdict(list)
        for key, val in counter.items():
            bucket[val].append(key)
        # print(bucket)
        res = []

        for i in range(len(s), 0, -1):
            # print(bucket[i])
            for c in bucket[i]:
                # print(c)
                res.append(c * i)
                # print(res)


        # for key, val in counter.items():
        #     oj.append([val, key])
        
        # print(oj)

        # oj.sort(reverse=True)
        # res = []
        # for bezat, char in oj:
        #     res.append(bezat * char)

        return "".join(res)

