import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1] * n
        k = len(primes)

        heap = [(primes[i], i, 0) for i in range(k)]
        heapq.heapify(heap)

        for i in range(1, n):
            ugly[i] = heap[0][0]

            while heap and heap[0][0] == ugly[i]:
                val, p_idx, u_idx = heapq.heappop(heap)
                heapq.heappush(heap, (primes[p_idx] * ugly[u_idx + 1], p_idx, u_idx + 1))

        return ugly[-1]