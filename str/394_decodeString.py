class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        index = 0

        while index < len(s):
            char = s[index]
            if char != "]":
                stack.append(char)
            else:
                sub_str = []
                while stack[-1] != "[":
                    sub_str.append(stack.pop())
                stack.pop()
                times, i = 0, 0
                while stack and stack[-1].isdigit():
                    times += int(stack.pop()) * (10 ** i)
                    i += 1
                for time in range(times):
                    for c in reversed(sub_str):
                        stack.append(c)
            index += 1
        return "".join(stack)


if __name__ == '__main__':
    s = "12[leetcode]"
    test = Solution()
    print(test.decodeString(s))
