class Solution:
    def numSub(self, s: str) -> int:
        ans, i = 0, 0
        while i < len(s):
            cnt = 0
            if s[i] == '0':
                i += 1
                continue
            else:
                while i < len(s):
                    if s[i] == '0':
                        break
                    else:
                        cnt += 1
                        i += 1
            ans += cnt
            ans += cnt * (cnt - 1) // 2
            i += 1
        return ans % (10 ** 9 + 7)


if __name__ == '__main__':
    s = "000"
    solution = Solution()
    print(solution.numSub(s))
