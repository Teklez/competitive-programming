class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i = 1
        j = len(skill) - 2
        res = [[skill[0],skill[-1]]]
        common = skill[0] + skill[-1]
        while i < j:
            if skill[i] + skill[j] != common:
                return -1
            res.append([skill[i], skill[j]])
            i +=1
            j -= 1
        summ = 0
        for pair in res:
            summ += pair[0]*pair[1]
        return summ



        