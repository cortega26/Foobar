"""
Hey, I Already Did That!
========================

Commander Lambda uses an automated algorithm to assign minions randomly to tasks, in order
to keep minions on their toes. But you've noticed a flaw in the algorithm -- it eventually
loops back on itself, so that instead of assigning new minions as it iterates, it gets
stuck in a cycle of values so that the same minions end up doing the same tasks over and
over again. You think proving this to Commander Lambda will help you make a case for your
next promotion.

You have worked out that the algorithm has the following process:

Start with a random minion ID n, which is a nonnegative integer of length k in base b
Define x and y as integers of length k. x has the digits of n in descending order, and
y has the digits of n in ascending order
Define z = x - y. Add leading zeros to z to maintain length k if necessary
Assign n = z to get the next minion ID, and go back to step 2
For example, given minion ID n = 1211, k = 4, b = 10, then x = 2111, y = 1112 and z = 2111 -
1112 = 0999. Then the next minion ID will be n = 0999 and the algorithm iterates again:
x = 9990, y = 0999 and z = 9990 - 0999 = 8991, and so on.

Depending on the values of n, k (derived from n), and b, at some point the algorithm reaches
a cycle, such as by reaching a constant value. For example, starting with n = 210022, k = 6,
b = 3, the algorithm will reach the cycle of values [210111, 122221, 102212] and it will
stay in this cycle no matter how many times it continues iterating. Starting with n = 1211,
the routine will reach the integer 6174, and since 7641 - 1467 is 6174, it will stay as that
value no matter how many times it iterates.

Given a minion ID as a string n representing a nonnegative integer of length k in base b,
where 2 <= k <= 9 and 2 <= b <= 10, write a function solution(n, b) which returns the
length of the ending cycle of the algorithm above starting with n. For instance, in the
example above, solution(210022, 3) would return 3, since iterating on 102212 would return
to 210111 when done in base 3. If the algorithm reaches a constant, such as 0, then the
length is 1.
"""


def number_to_base(n: int, base: int) -> str:
    """
    Given an integer `n` and a base `base`, this function returns the string
    representation of `n` in that base.

    For example, number_to_base(31, 16) returns "1F".

    Parameters:
    -----------
    n: int
        The number to convert to a string in the given base.
    base: int
        The base to use for the string representation.

    Returns:
    --------
    str
        The string representation of `n` in the given base.
    """
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    return "".join(str(d) for d in digits[::-1])


def solution(n: str, base: int) -> int:
    """
    Given a minion ID as a string `n` representing a nonnegative integer of length
    `k` in base `b`, where `2 <= k <= 9` and `2 <= b <= 10`, this function returns
    the length of the ending cycle of the algorithm described in the problem
    statement, starting with `n`.

    Parameters:
    -----------
    n: str
        A string representing the minion ID to start with.
    base: int
        An integer representing the base of the minion ID.

    Returns:
    --------
    int
        The length of the ending cycle of the algorithm starting with `n`.
    """
    k = len(n)
    loop = False
    seen = []
    while not loop:
        n_asc = "".join(sorted(n))
        n_des = "".join(sorted(n, reverse=True))
        res = number_to_base(int(n_des, base) - int(n_asc, base), base)
        res.zfill(k)
        if res in seen:
            loop = True
        else:
            seen.append(res)
        n = res
    return len(seen) - seen.index(res)


if __name__ == "__main__":
    print(solution("123456779", 10))
