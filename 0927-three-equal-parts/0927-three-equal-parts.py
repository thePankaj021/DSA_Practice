class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones = sum(arr)

        if ones == 0:
            return [0, 2]

        if ones % 3:
            return [-1, -1]

        k = ones // 3
        first = second = third = -1
        cnt = 0

        for i, bit in enumerate(arr):
            if bit:
                cnt += 1
                if cnt == 1:
                    first = i
                elif cnt == k + 1:
                    second = i
                elif cnt == 2 * k + 1:
                    third = i

        length = len(arr) - third

        if (first + length <= second and
            second + length <= third):

            if (arr[first:first + length] ==
                arr[second:second + length] ==
                arr[third:]):
                return [first + length - 1,
                        second + length]

        return [-1, -1]