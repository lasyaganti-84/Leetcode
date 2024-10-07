class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = defaultdict(int)
        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        top_k_values = list(dict(sorted(dict1.items() , key = lambda item: item[1] , reverse = True)[:k]))
        
        return top_k_values
        
         
