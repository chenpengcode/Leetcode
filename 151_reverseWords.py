import collections


class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.strip()
        s_list = s.split()
        tmp = reversed(s_list)
        ans = " ".join(tmp)
        return ans

    def reverseWords_2(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1
        while right >= left and s[right] == ' ':
            right -= 1

        d, word = collections.deque(), []
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1

        d.appendleft(''.join(word))
        return ' '.join(d)


if __name__ == '__main__':
    s = "a good   example "
    test = Solution()
    print(test.reverseWords_2(s))
