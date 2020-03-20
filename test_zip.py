A = ["zyx", "wvu", "tsr"]

ans = 0
for col in zip(*A):
    if any(col[i] > col[i + 1] for i in range(len(col) - 1)):
        ans += 1
# print(ans)


arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
dict_arr = {}
for i in arr:
    dict_arr[i] = 0
for i in arr:
    dict_arr[i] += 1

set_1 = set(list(dict_arr.values()))
# print(set_1)
# print(len(set_1))
# print(len(dict_arr))

dict_test = {0}
print(dict_test)