"""
The cake is not a lie
=====================
Commander Lambda has had an incredibly successful week: she completed the
first test run of her LAMBCHOP doomsday device, she captured six key members
of the Bunny Rebellion, and she beat her personal high score in Tetris. To
celebrate, she's ordered cake for everyone - even the lowliest of minions!
But competition among minions is fierce, and if you don't cut exactly equal
slices of cake for everyone, you'll get in big trouble.

The cake is round, and decorated with M&Ms in a circle around the edge. But
while the rest of the cake is uniform, the M&Ms are not: there are multiple
colors, and every minion must get exactly the same sequence of M&Ms. Commander
Lambda hates waste and will not tolerate any leftovers, so you also want to
make sure you can serve the entire cake.

To help you best cut the cake, you have turned the sequence of colors of the
M&Ms on the cake into a string: each possible letter (between a and z)
corresponds to a unique color, and the sequence of M&Ms is given clockwise
(the decorations form a circle around the outer edge of the cake).

Write a function called answer(s) that, given a non-empty string less than
200 characters in length describing the sequence of M&Ms, returns the
maximum number of equal parts that can be cut from the cake without leaving
any leftovers.
"""

def solution(s: str):
    """
    Given a non-empty string `s` of length at most 200 characters, representing
    a sequence of M&Ms, this function returns the maximum number of equal parts
    that can be cut from the sequence without leaving any leftovers. 

    The function first calculates all the divisors of the length of the sequence
    and then checks whether the sequence can be formed by concatenating a
    smaller substring `divisors_list[len(divisors_list) - index - 1]` times,
    where the length of the smaller substring is `size // divisors_list[index]`. 

    If such a substring is found, the function returns the maximum number of
    equal parts that can be cut from the sequence, which is equal to
    `size // divisors_list[index]`. Otherwise, the function returns None.
    """
    size = len(s)
    divisors_list = [i for i in range(1, size + 1) if size % i == 0]
    for index, divisor in enumerate(divisors_list):
        if s == s[:divisor] * divisors_list[len(divisors_list) - index - 1]:
            return size // divisors_list[index]
    return None


if __name__ == "__main__":
    print(solution('abcabcabcgabcabcabcgabcabcabcgabcabcabcg'))
