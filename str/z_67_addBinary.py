class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lista = list(reversed([int(x) for x in a]))
        listb = list(reversed([int(x) for x in b]))
        if len(a) < len(b):
            lista, listb = listb, lista
        increment = 0
        for i in range(len(lista)):
            tmp = lista[i]
            if i < len(listb):
                lista[i] = (tmp + listb[i] + increment) % 2
                increment = (tmp + listb[i] + increment) // 2
            else:
                lista[i] = (tmp + increment) % 2
                increment = (tmp + increment) // 2
        if increment == 1:
            lista.append(1)
        print(lista)
        ans = ''.join([str(x) for x in reversed(lista)])
        return ''.join(ans)


if __name__ == '__main__':
    a = '11'
    b = '1'
    solution = Solution()
    print(solution.addBinary(a, b))
