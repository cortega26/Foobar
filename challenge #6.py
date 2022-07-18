"""
Bomb, baby
==========
You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in order to do so, you need to
deploy special self-replicating bombs designed for you by the brightest scientists on Bunny Planet. There are
two types: Mach bombs (M) and Facula bombs (F). The bombs, once released into the LAMBCHOP's inner workings,
will automatically deploy to all the strategic points you've identified and destroy them at the same time.

But there's a few catches. First, the bombs self-replicate via one of two distinct processes: Every Mach bomb
retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created; Every Facula bomb
spontaneously creates a Mach bomb.

For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 3 Mach bombs and 5 Facula
bombs, or 5 Mach bombs and 2 Facula bombs. The replication process can be changed each cycle.

Second, you need to ensure that you have exactly the right number of Mach and Facula bombs to destroy the LAMBCHOP
device. Too few, and the device might survive. Too many, and you might overload the mass capacitors and create a
singularity at the heart of the space station - not good!

And finally, you were only able to smuggle one of each type of bomb - one Mach, one Facula - aboard the ship when
you arrived, so that's all you have to start with. (Thus it may be impossible to deploy the bombs to destroy the
LAMBCHOP, but that's not going to stop you from trying!)

You need to know how many replication cycles (generations) it will take to generate the correct amount of bombs
to destroy the LAMBCHOP. Write a function solution(M, F) where M and F are the number of Mach and Facula bombs
needed. Return the fewest number of generations (as a string) that need to pass before you'll have the exact
number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M and F
will be string representations of positive integers no larger than 10^50. For example, if M = "2" and F = "1",
one generation would need to pass, so the solution would be "1". However, if M = "2" and F = "4", it would not
be possible.
"""

# To solve this problem we have to resign to the idea of going from A to B, as in trying to find the shortest
# path from the root to the leaf. We, instead, approach the problem in the opposite direction: starting from B
# and looking at the route to A. According to the problem you will be given two positive integers (M, F) and
# the ONLY way to get there according to the instructions is by doing (M+F, F) or (M, F+M) in a previous step,
# in either case, you can't get the smaller number (M or F) by adding the larger in a previous step, this means
# the larger number will ALWAYS be the one who got added the number of its replicant partner in the previous step.

# For instance, if you have (59, 95), who got the summation? M or F? We know for sure it was F because there is
# no positive integer that added to 95 will result in 59.


def solution(m, f):
    m, f = int(m), int(f)
    replications = 0
    while (m >= 1 and f >= 1):
        if m == 1 and f == 1:
            return str(replications)
        if m == 1 or f == 1:
            return str(replications + abs(m - f))
        if m > f:
            replications += m // f
            m = m % f
        else:
            replications += f // m
            f = f % m
    return 'impossible'


if __name__ == "__main__":
    solution(459, 26)
