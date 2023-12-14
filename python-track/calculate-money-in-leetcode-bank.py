class Solution:
    def totalMoney(self, n: int) -> int:
        week = n // 7
        total = week * 28
        total += (7 * week *( week - 1))//2

        if (n % 7):
            remain = n % 7
            added = week + 1
            for i in range(remain):
                total += added
                added += 1

        return total