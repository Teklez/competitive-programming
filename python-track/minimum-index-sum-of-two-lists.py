class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mapped = {}
        for i in range(len(list1)):
            mapped[list1[i]] = i
        minm = len(list1) + len(list2)
        res = []
        for j in range(len(list2)):
            if list2[j] in mapped:
                index_sum = j + mapped[list2[j]]
                if index_sum < minm:
                    res = []
                    res.append(j)
                    minm = index_sum
                elif index_sum == minm:
                    res.append(j)
        return [list2[j] for j in res]
            
            
        return res

