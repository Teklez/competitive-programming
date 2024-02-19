class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store = {}
        m_stack = []
        for i in range(len(nums2)):
                while m_stack and m_stack[-1] < nums2[i]:
                    store[m_stack.pop()] = nums2[i]
                m_stack.append(nums2[i])
        return [store.get(num,-1) for num in nums1]

        