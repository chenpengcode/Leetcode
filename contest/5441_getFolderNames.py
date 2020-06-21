from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        d = {}
        for i in range(len(names)):

            if names[i] not in d.keys():
                d[names[i]] = 0
                ans.append(names[i])
            else:
                cnt = d[names[i]] + 1
                new_name = names[i] + "({})".format(str(cnt))
                while new_name in d.keys():
                    cnt += 1
                    new_name = names[i] + "({})".format(str(cnt))
                d[new_name] = 0
                ans.append(new_name)
        return ans


if __name__ == '__main__':
    names = ["kaido", "kaido(1)", "kaido", "kaido(1)", "kaido(2)"]
    solution = Solution()
    print(solution.getFolderNames(names))
