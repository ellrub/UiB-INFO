# Assignment 7
# ---------- Question 1 ---------- #
# The Big O notation is O(n^3)

# -------------------------------- #

# ---------- Question 2 ---------- #
# The Big O notation is O(n log n)
# This is because the outer loop runs n times and the inner loop runs log n times.
# We multiply the two loops to get O(n log n)

# -------------------------------- #

# ---------- Question 3 ---------- #
# This function is a typical bubble sort algorithm, and therefore i already know that the bigO is O(n^2)
# This is because the outer loop runs n times and the inner loop runs n times, we multiply the two and get O(n^2)

# -------------------------------- #

# ---------- Question 4 ---------- #
def solve_problem(S):
    A = []
    usage = 0
    for i in range(len(S)):
        usage += S[i]
        avarage = usage / (i + 1)
        A.append(avarage)
    return A

# The function take a list as input, which represents daily usage. It then iterates over the list at index i for each day i. and adds it to the total usage.
# It the calculates the avarage usage for each day and appends it to the list A. When the loop is complete, the function then returns the list A.
# The BigO notation is O(n), because the function iterates over the list n once.