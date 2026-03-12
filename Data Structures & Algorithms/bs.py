A = [-3, -1, 0, 1, 4, 7]

# Naive O(n) searching:
if -1 in A:
    print(True)

# Traditional binary search - O(logN)
def binary_search(arr, target):
    N = len(arr)

    L = 0
    R = len(A) - 1

    while L <= R:
        M = L + ((R - L) // 2)
        
        if arr[M] == target:
            return True
        elif target < arr[M]:
            R = M - 1
        else:
            L = M + 1

    return False

print(binary_search(A, 4))

# Based on a condition binary search
# [F, F, F, T, T, T]

B = [False, False, False, True, True, True]

def binary_search_condition(arr):
    N = len(arr)
    L = 0
    R = N - 1

    while L < R:
        M = (L + R) // 2

        if arr[M]:
            R = M
        else:
            L = M + 1
    
    return L

print(binary_search_condition(B))