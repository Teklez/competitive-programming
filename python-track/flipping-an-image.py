class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in image:
            i = 0
            j = len(row) - 1
            while i < j:
                row[i], row[j] = row[j], row[i]
                i += 1
                j -= 1
            for i in range(len(row)):
                if row[i] == 1:
                    row[i] = 0
                else:
                    row[i] = 1
        return image
                