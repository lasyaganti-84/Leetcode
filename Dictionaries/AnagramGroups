class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            print(s)
            for c in s:
                count[ord(c) - ord("a")] += 1
                print(c)
            res[tuple(count)].append(s)
            print(res)

        return res.values()

