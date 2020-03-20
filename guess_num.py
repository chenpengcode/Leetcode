class Solution(object):
    def game(self, guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """
        rst = 0
        len_all = len(guess) + len(answer)
        list_all = guess + answer
        print(len_all)
        for i in range(len(guess)):
            if list_all[i] == list_all[i + len_all // 2]:
                rst += 1

        return rst

    def game_2(self, guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """
        rst = 0
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                rst += 1

        return rst


if __name__ == '__main__':
    guess = [1, 2, 3]
    answer = [1, 2, 3]
    # print(guess + answer)
    # guess.extend(answer)
    # print(guess)
    test = Solution()
    print(test.game_2(guess, answer))
