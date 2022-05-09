"""
Fuel Injection Perfection
=========================

Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for the
LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP -- and maybe sneak in
a bit of sabotage while you're at it -- so you took the job gladly. 

Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each
need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to
figure out the most efficient way to sort and shift the pellets down to a single pellet at a time. 

The fuel control mechanisms have three operations: 

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter
pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of
operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number
up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

For example:
solution(4) returns 2: 4 -> 2 -> 1
solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
"""


def solution(n):
    n = int(n)
    operations = 0
    
    if (n >= 1) and (n <= 3):
        return n - 1
        
    while n > 1:
        
        # Any even number will be divided by two
        # until we get an odd number. Since we are
        # guaranteed the number is divisible by
        # two we use floor division to avoid stack
        # overflow with strings of 309 digits.
        if n % 2 == 0:
            n = n // 2

        # Any odd number has two even neighbors:
        # a) One can be divided by two just ONCE, and
        # b) The other can be divided by two MORE than once
        # We then discard option a)
        elif (n-1) % 4 == 0 or n == 3:
            n -= 1
        else:
            n += 1

        operations += 1
        
    return operations


if __name__ == "__main__":
    print(solution('123852951'))
