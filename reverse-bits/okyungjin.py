"""
https://leetcode.com/problems/reverse-bits/description/

Time: O(1)
Space: O(1)

예시:
    n      :  1  1  0  1
    result :  0  0  0  0

    1) `n & 1`: n의 끝자리 추출
    n      :  1  1  0 [1] 

    2) `result << 1`: 비트를 왼쪽으로 밀어 빈 공간 확보
    result :  0  0  0 [ ]

    3) `|`: 가져온 비트를 빈자리에 결합
    result :  0  0  0 [1]

    4) `n >> 1`: 사용한 비트 오른쪽으로 밀어서 버리기
    n      :  [0]  1  1  0
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        BIT_LEN = 32
        result = 0

        for _ in range(BIT_LEN):
            result = (result << 1) | (n & 1)
            n = n >> 1

        return result
