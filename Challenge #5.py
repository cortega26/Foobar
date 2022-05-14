"""
Doomsday Fuel
=============

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts
as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form.
There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel. 

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end
state of a given ore sample. You have carefully studied the different structures that the ore can take and which
transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed.
That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might
be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized
more exotic forms that the ore can become, but you haven't seen all of them.

Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state
has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of
each terminal state, represented as the numerator for each state, then the denominator for all of them at the end
and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in,
there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable
state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation,
as long as the fraction is simplified regularly. 

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].
"""

# In order to solve this problem we need to transform the given matrix
# into its markovian canonical form which is:
#
#      Q | R
# P = -------
#      0 | I
#
#
# Also please be aware this exercise can be solved with a small fraction of this code
# (yes, this is verbose solution) by using a module like Numpy or Scipy and Fractions.


def solution(m):
   
    matrix = transpose(reorder2(transpose(normalize(reorder(m)))))
    non_id = q_size(m)
    id_mat = identity_matrix(non_id)
    q_mat = matrix_q(matrix, non_id)
    i_minus_q = matrix_subtraction(id_mat, q_mat)
    n_mat = matrix_inverse(i_minus_q)
    r_mat = matrix_r(matrix, non_id, non_id, len(m))
    num_values = len(m) - non_id
    res = matrix_multiplication(n_mat, r_mat)
    res = res[0:1][0]
    flag = False
    for i in range(1, (2 ** 31)):
        if flag:
            break
        coincidences = 0
        for j in range(num_values):
            if round((res[j] * i), 10) == int(round((res[j] * i), 10)):
                coincidences += 1
                if coincidences == num_values:
                    denominator = i
                    flag = True
    sf = []
    for element in res:
        element *= denominator
        if round(element, 10) == int(round(element, 10)):
            element = int(round(element, 10))
        sf.append(element)
    sf.append(denominator)
    return sf
  

# All rows must add 1, so add up all indices that sum is our denominator
def normalize(m):
    matrix = []
    for array in m:
        row_p = []
        for element in array:
            if element > 0:
                normalized = element / sum(array)
            else:
                normalized = element
            row_p.append(normalized)
        matrix.append(row_p)
    return matrix
  

# Send all rows of zeros down and change to 1 on absorbing states
def reorder(m): 
    new_mat = []
    ind = []
    for i, array in enumerate(m):
        if sum(array) > 0:
            new_mat.append(array)
        else:
            ind.append(i)
    zero_array = [[0 for _ in range(len(m))] for _ in range(len(ind))]
    for idx, array in enumerate(zero_array):
        array[ind[idx]] = -1
    f_mat = new_mat + zero_array
    return f_mat


# After transposing we send all absorbing states down again
# To obtain the markov matrix in its cannonical form
def reorder2(m):
    up_mat = []
    down_mat = []
    for i, array in enumerate(m):
        if array.count(-1) == 0:
            up_mat.append(array)
        else:
            down_mat.append(array)
    fin = up_mat + down_mat
    for array in fin:
        for elem in array:
            if elem == -1:
                elem = 1
    return up_mat + down_mat


# Function to transpose matrix so we rearrange it later
def transpose(m):
    mat = []
    for i in range(len(m)):
        row = []
        for j in range(len(m[0])):
            row.append(m[j][i])
        mat.append(row)
    return mat


# Simple function to build an identity matrix of a given size
def identity_matrix(size):
    matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        matrix[i][i] = 1
    return matrix


# Once we have the matrix in its canonical form we calculate Q size
def q_size(m):
    id = 0
    for array in m:
        if array.count(0) == len(m):
            id += 1
    return len(m) - id   


# Extracting Q from P
def matrix_q(matrix, size):
    mat_q = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(matrix[i][j])
        mat_q.append(row)
    return mat_q
  

# Extracting R from P
def matrix_r(matrix, final_row, initial_column, final_column):
    mat_r = []
    for i in range(final_row):
        row = []
        for j in range(initial_column, final_column):
            row.append(matrix[i][j])
        mat_r.append(row)
    return mat_r


# Function to obtain I - Q
def matrix_subtraction(a, b):
    matrix = [[0 for _ in range(len(a))] for _ in range(len(a[0]))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            matrix[i][j] = a[i][j] - b[i][j]
    return matrix


def matrix_multiplication(a, b):
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result


def eliminate(r1, r2, col, target=0):
    fac = (r2[col] - target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]


def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i + 1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
        for j in range(i + 1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a


def matrix_inverse(a):
    tmp = [[] for _ in a]
    for i, row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0] * i + [1] + [0] * (len(a) - i - 1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i]) // 2:])
    return ret
  

if __name__ == "__main__":
  print(solution([[0, 1, 0, 0, 0, 1],
                  [4, 0, 0, 3, 2, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0]]))
