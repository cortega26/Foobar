"""
Bomb, baby
==========
You're so close to destroying the LAMBCHOP doomsday device you can taste it!
But in order to do so, you need to deploy special self-replicating bombs
designed for you by the brightest scientists on Bunny Planet. There are two
types: Mach bombs (M) and Facula bombs (F). The bombs, once released into the
LAMBCHOP's inner workings, will automatically deploy to all the strategic
points you've identified and destroy them at the same time.

But there's a few catches. First, the bombs self-replicate via one of two
distinct processes: Every Mach bomb retrieves a sync unit from a Facula bomb;
for every Mach bomb, a Facula bomb is created; Every Facula bomb spontaneously
creates a Mach bomb.

For example, if you had 3 Mach bombs and 2 Facula bombs, they could either
produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs.
The replication process can be changed each cycle.

Second, you need to ensure that you have exactly the right number of Mach and
Facula bombs to destroy the LAMBCHOP device. Too few, and the device might
survive. Too many, and you might overload the mass capacitors and create a
singularity at the heart of the space station - not good!

And finally, you were only able to smuggle one of each type of bomb - one Mach,
one Facula - aboard the ship when you arrived, so that's all you have to start
with. (Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP,
but that's not going to stop you from trying!)

You need to know how many replication cycles (generations) it will take to
generate the correct amount of bombs to destroy the LAMBCHOP. Write a function
solution(M, F) where M and F are the number of Mach and Facula bombs needed.
Return the fewest number of generations (as a string) that need to pass before
you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or
the string "impossible" if this can't be done! M and F will be string
representations of positive integers no larger than 10^50. For example, if M =
"2" and F = "1", one generation would need to pass, so the solution would be
"1". However, if M = "2" and F = "4", it would not be possible.
"""


def solution(m, f):
    """
    This script solves the "Bomb, baby" problem. Given the number of Mach bombs (M)
    and Facula bombs (F) needed to destroy a doomsday device, the function
    solution(M, F) returns the fewest number of generations it will take to generate
    the exact number of bombs necessary, or "impossible" if this can't be done.

    To solve the problem, the script starts from the target number of bombs and works
    backwards, using a simple algorithm that computes the number of replicant partners
    needed to generate the required number of bombs. The script also checks for edge
    cases where the starting values are 1 or where the required number of bombs is
    not achievable.
    
    Args:
        m (str): A string representing the number of Mach bombs needed to destroy
            the LAMBCHOP device. A positive integer no larger than 10^50.
        f (str): A string representing the number of Facula bombs needed to
            destroy the LAMBCHOP device. A positive integer no larger than 10^50.

    Returns:
        str: The fewest number of generations that need to pass before you'll have
            the exact number of bombs necessary to destroy the LAMBCHOP, or the
            string "impossible" if this can't be done.
    """
    m, f = int(m), int(f)

    if m == 1 and f == 1:
        return '0'

    replications = 0
    while m > 1 and f > 1:
        if m > f:
            replications += m // f
            m %= f
        else:
            replications += f // m
            f %= m

    if m == 1 or f == 1:
        return str(replications + abs(m - f))

    return 'impossible'


if __name__ == "__main__":
    print(solution('459', '26'))

