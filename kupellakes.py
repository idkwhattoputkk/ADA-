# function to calculate the difference between the sums of left and right subtrees
def subtree_diff(node):
    if not node:
        return 0
    return node.val + subtree_diff(node.left) - subtree_diff(node.right)

# function to build kuPellaKeS BST
def build_kupellakes_bst(arr, l, r):
    if l > r:
        return None
    if l == r:
        return TreeNode(arr[l])
    
    # sort the array and find the mid-point
    sorted_arr = sorted(arr[l:r+1])
    mid = (l + r) // 2
    root = TreeNode(sorted_arr[mid])
    
    # recursively build left and right subtrees
    root.left = build_kupellakes_bst(arr, l, mid-1)
    root.right = build_kupellakes_bst(arr, mid+1, r)
    
    return root

# function to generate string representation of BST
def bst_to_string(node):
    if not node:
        return ""
    if not node.left and not node.right:
        return str(node.val)
    if not node.right:
        return str(node.val) + "(" + bst_to_string(node.left) + ")"
    return str(node.val) + "(" + bst_to_string(node.left) + "," + bst_to_string(node.right) + ")"

# main function to solve the problem
def solve_kupellakes_bst():
    t = int(input())  # number of test cases
    for i in range(1, t+1):
        n = int(input())  # number of values in the BST
        arr = list(map(int, input().split()))  # array of values
        root = build_kupellakes_bst(arr, 0, n-1)  # build the kuPellaKeS BST
        result = bst_to_string(root)  # get string representation of BST
        print("Case #{}: {}".format(i, result))

# run the main function
solve_kupellakes_bst()
import sys
from typing import List


def rec(A: List[int], a: int, b: int) -> str:
    if a > b:
        return ""

    if a == b:
        return str(A[a])

    best = a
    best_diff = 1 << 30
    best_left = 0

    for r in range(a, b + 1):
        if r < b and A[r + 1] == A[r]:
            continue
        L = S[r] - S[a]
        R = S[b + 1] - S[r + 1]
        diff = L - R
        if diff < 0:
            diff = -diff
        if diff < best_diff or (diff == best_diff and L > best_left):
            best = r
            best_diff = diff
            best_left = L

    left_subtree = rec(A, a, best - 1)
    right_subtree = rec(A, best + 1, b)

    if left_subtree != "":
        left_subtree += ","

    return f"{A[best]}({left_subtree}{right_subtree})"


def solve_case(case_num: int, A: List[int]) -> str:
    A.sort()

    S = [0] * (len(A) + 1)
    for i in range(1, len(S)):
        S[i] = S[i - 1] + A[i - 1]

    return f"Case #{case_num}: {rec(A, 0, len(A) - 1)}"


if __name__ == "__main__":
    num_cases = int(input())
    for i in range(num_cases):
        n, *books = map(int, input().split())
        print(solve_case(i + 1, books))
