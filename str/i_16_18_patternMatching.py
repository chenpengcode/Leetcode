import collections


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        cnt_a = sum(1 for c in pattern if c == 'a')
        cnt_b = len(pattern) - cnt_a
        if cnt_a < cnt_b:
            cnt_a, cnt_b = cnt_b, cnt_a
            pattern = ''.join('a' if c == 'b' else 'b' for c in pattern)

        if not value:
            return cnt_b == 0
        if not pattern:
            return False

        for len_a in range(len(value) // cnt_a + 1):
            rest = len(value) - cnt_a * len_a
            if (cnt_b == 0 and rest == 0) or (cnt_b != 0 and rest % cnt_b == 0):
                len_b = 0 if cnt_b == 0 else rest // cnt_b
                pos, correct = 0, True
                val_a, val_b = None, None
                for c in pattern:
                    if c == 'a':
                        sub = value[pos: len_a + pos]
                        if not val_a:
                            val_a = sub
                        elif sub != val_a:
                            correct = False
                            break
                        pos += len_a
                    else:
                        sub = value[pos: len_b + pos]
                        if not val_b:
                            val_b = sub
                        elif sub != val_b:
                            correct = False
                            break
                        pos += len_b
                if correct and val_a != val_b:
                    return True

        return False
