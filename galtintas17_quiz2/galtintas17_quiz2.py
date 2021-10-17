from math import inf

arrays = [[1, 2, 3, 2, 6, 6],
          [3, 2, 9, 1, 8, 2, 0, 4, 5],
          [3, 2, 6, 1, 8, 2, 0, 4, 5],
          [1, 3, 2, 2, 3],
          [1, 0, 3, 2],
          [2, 3, 0]]


def find_jumps_from(arr, i, jumps):
    """     finds the minimum number of jumps from i to the end of the array    """
    # check if we can directly jump to the end
    if arr[i] + i >= len(arr):
        return 1
    if arr[i] == 0:
        return -1
    min_jumps = inf
    for j in range(i + 1, min(len(arr), i + 1 + arr[i])):
        # pass dead end
        if jumps[j] <= 0:
            continue
        min_jumps = min(min_jumps, jumps[j])
    # if the end is unreachable, return -1
    if min_jumps == inf:
        return -1
    return min_jumps + 1


def find_min_jumps(arr):
    """     for a given array, finds the minimum number of jumps from the beginning to the end      """
    n = len(arr)
    # initialize jumps array
    jumps = [-1] * n
    for i in range(n - 1, -1, -1):
        jumps[i] = find_jumps_from(arr, i, jumps)
    print(
        f"For the following array: {arr}\n\tThe dynamic programming table looks like as follows: {jumps}\n\t"
        f"Resulting in {jumps[0]} total jumps")
    print("-" * 15)
    return jumps[0]


def main():
    for arr in arrays:
        find_min_jumps(arr)


if __name__ == "__main__":
    main()
