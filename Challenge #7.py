"""
Running with Bunnies
====================

You and the bunny workers need to get out of this collapsing death trap of a space station -- and fast!
Unfortunately, some of the bunnies have been weakened by their long work shifts and can't run very fast. Their
friends are trying to help them, but this escape would go a lot faster if you also pitched in. The defensive
bulkhead doors have begun to close, and if you don't make it through in time, you'll be trapped! You need to
grab as many bunnies as you can and get through the bulkheads before they close. 

The time it takes to move from your starting point to all of the bunnies and to the bulkhead will be given to
you in a square matrix of integers. Each row will tell you the time it takes to get to the start, first bunny,
second bunny, ..., last bunny, and the bulkhead in that order. The order of the rows follows the same pattern
(start, each bunny, bulkhead). The bunnies can jump into your arms, so picking them up is instantaneous, and
arriving at the bulkhead at the same time as it seals still allows for a successful, if dramatic, escape. (Don't
worry, any bunnies you don't pick up will be able to escape with you since they no longer have to carry the ones
you did pick up.) You can revisit different spots if you wish, and moving to the bulkhead doesn't mean you have
to immediately leave -- you can move to and from the bulkhead to pick up additional bunnies if time permits.

In addition to spending time traveling between bunnies, some paths interact with the space station's security
checkpoints and add time back to the clock. Adding time to the clock will delay the closing of the bulkhead
doors, and if the time goes back up to 0 or a positive number after the doors have already closed, it triggers
the bulkhead to reopen. Therefore, it might be possible to walk in a circle and keep gaining time: that is,
each time a path is traversed, the same amount of time is used or added.

Write a function of the form solution(times, time_limit) to calculate the most bunnies you can pick up and which
bunnies they are, while still escaping through the bulkhead before the doors close for good. If there are multiple
sets of bunnies of the same size, return the set of bunnies with the lowest worker IDs (as indexes) in sorted
order. The bunnies are represented as a sorted list by worker ID, with the first bunny being 0. There are at most
5 bunnies, and time_limit is a non-negative integer that is at most 999.

For instance, in the case of
[
  [0, 2, 2, 2, -1],  # 0 = Start
  [9, 0, 2, 2, -1],  # 1 = Bunny 0
  [9, 3, 0, 2, -1],  # 2 = Bunny 1
  [9, 3, 2, 0, -1],  # 3 = Bunny 2
  [9, 3, 2, 2,  0],  # 4 = Bulkhead
]
and a time limit of 1, the five inner array rows designate the starting point, bunny 0, bunny 1, bunny 2, and the 
bulkhead door exit respectively. You could take the path:

Start End Delta Time Status
    -   0     -    1 Bulkhead initially open
    0   4    -1    2
    4   2     2    0
    2   4    -1    1
    4   3     2   -1 Bulkhead closes
    3   4    -1    0 Bulkhead reopens; you and the bunnies exit

With this solution, you would pick up bunnies 1 and 2. This is the best combination for this space station hallway, so the solution is [1, 2].
"""

from itertools import permutations

def solution(times, time_limit):
    nodes = len(times)
    inner_nodes = nodes - 2
    g = Graph(nodes)
    [[g.addEdge(i, j, element) for j, element in enumerate(array) if i != j] for i, array in enumerate(times)]
    all_permutations = []
    for k in range(nodes - 1):
        inner_permutations = [list(j) for j in list(permutations([i for i in range(1, nodes - 1)], (inner_nodes - k)))]
        for array in inner_permutations:
            array = [0] + array + [nodes - 1]
            all_permutations.append(array)

    distances = [g.BellmanFord(i) for i in range(nodes)]

    if None in distances: # This is to ask if a negative cycle exists
        solut = [i for i in range(nodes)]
        solut = solut[1:-1]
        return [i - 1 for i in solut] 
   
    for i in range(nodes - 1):
        for permut in all_permutations:
            used_time = 0
            min_time = float("Inf")
            if len(permut) == nodes - i:
                for j in range(len(permut)-1):
                    for array in distances:
                        for distance in array:
                            if permut[j] == distance[0] and permut[j+1] == distance[1]:
                                used_time += distance[2]
            else:
                continue
            if used_time < min_time:
                min_time = used_time
                if min_time <= time_limit:
                    permut = permut[1:-1]
                    permut = [i - 1 for i in permut]
                    permut.sort()
                    return permut


class Graph:
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
 
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
         
    def printArr(self, dist, src):
        return [[src, i, dist[i]] for i in range(self.V)]
      
    def BellmanFord(self, src):
 
        dist = [float("Inf")] * self.V
        dist[src] = 0
 
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
 
        for u, v, w in self.graph:
            if dist[u] != float(u"Inf") and dist[u] + w < dist[v]:
                return None
                         
        return self.printArr(dist, src)
      
      
solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)
