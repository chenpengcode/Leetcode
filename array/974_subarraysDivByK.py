from typing import List

"""
pre_sum[i] = A[0] + A[1] + A[2] + ... + A[i]
A[i] = pre_sum[i] - (A[0] + A[1] + A[2] + ... + A[i - 1]) = pre_sum[i] - pre_sum[i - 1]
A[i] + A[i + 1] + A[i + 2] + ... + A[j] = pre_sum[j] - pre_sum[i - 1]
同余定理：
(pre_sum[j] - pre_sum[i]) % K = 0 
----> pre_sum[i] % K - pre_sum[j] % K = 0
----> pre_sum[i] % K = pre_sum[j] % K
前缀和模K相同的元素子数组之和
=====>
前缀和模K相等的子数组的数目
=====>

"""


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        ans = 0

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if sum(A[i: j]) % K == 0:
                    ans += 1
        return ans

    def subarraysDivByK_brute(self, A: List[int], K: int) -> int:
        ans = 0
        for i in range(len(A)):
            sum = 0
            for j in range(i, len(A)):
                sum += A[j]
                if sum % K == 0:
                    ans += 1
        return ans

    def subarraysDivByK_pre(self, A: List[int], K: int) -> int:
        record = {0: 1}
        total, ans = 0, 0
        for elem in A:
            total += elem
            modulus = total % K
            same = record.get(modulus, 0)
            ans += same
            record[modulus] = same + 1

        return ans

    def subarraysDivByK_presum(self, A: List[int], K: int) -> int:
        ans, pre_sum = 0, 0

        mod = [1]
        for num in A:
            pre_sum += num
            m = pre_sum % K
            ans += mod[m]
            mod[m] += 1
        return ans
