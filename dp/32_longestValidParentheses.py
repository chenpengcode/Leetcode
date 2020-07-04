class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def is_valid(s):
            stack = []
            for c in s:
                if c == '(':
                    stack.append(c)
                elif stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            return stack == []

        n = len(s)
        if n < 2:
            return 0
        for i in range(n if n % 2 == 0 else n - 1, 0, -2):
            for j in range(n - i + 1):
                if is_valid(s[j:j + i]):
                    return i
        return 0

    def longestValidParentheses_dp(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        for i in range(n):
            if s[i] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
        return max(dp)

    def longestValidParentheses_stack(self, s: str) -> int:
        ans = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
                continue
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                ans = max(ans, i - stack[-1])
        return ans

    def longestValidParentheses_double(self, s: str) -> int:
        left = right = 0
        ans = 0
        for c in s:
            if c == '(':
                left += 1
            if c == ')':
                right += 1
            if left == right:
                ans = max(ans, left * 2)
            elif right > left:
                left = right = 0
        left = right = 0
        for c in reversed(s):
            if c == '(':
                left += 1
            if c == ')':
                right += 1
            if left == right:
                ans = max(ans, left * 2)
            elif left > right:
                left = right = 0
        return ans


if __name__ == '__main__':
    s = "()(()"
    solution = Solution()
    print(solution.longestValidParentheses_double(s))
