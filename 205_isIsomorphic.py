class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
            s_len = len(s)
            t_len = len(t)
            if s_len != t_len:
                return False

            s_dict = {}
            for i in range(s_len):
                if s[i] in s_dict:
                    if t[i] != s_dict[s[i]]:
                        return False
                elif t[i] in s_dict.values():
                    return False
                else:
                    s_dict.update({s[i]: t[i]})

            return True


if __name__ == '__main__':
    test = Solution()
    s = 'foo'
    t = 'bbb'
    print(test.isIsomorphic(s, t))
