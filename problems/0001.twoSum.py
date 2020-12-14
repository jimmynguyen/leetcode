# https://leetcode.com/problems/two-sum/
import util


def twoSum_bruteForce(nums,target):
    #  time complexity: O(n^2)
    # space complexity: O(1)
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return [i,j]
    raise Exception("no possible solution")


def twoSum_twoPassHashTable(nums,target):
    #  time complexity: O(n)
    # space complexity: O(n)
    n = len(nums)
    table = dict()
    for i in range(n):
        table[nums[i]] = i
    for i in range(n):
        complement = target - nums[i]
        j = table.get(complement)
        if j is not None and j != i:
            return [i,j]
    raise Exception("no possible solution")


def twoSum_onePassHashTable(nums,target):
    #  time complexity: O(n)
    # space complexity: O(n)
    n = len(nums)
    table = dict()
    for i in range(n):
        complement = target - nums[i]
        if complement in table:
            return [table.get(complement),i]
        table[nums[i]] = i
    raise Exception("no possible solution")


if __name__ == "__main__":
    solutions = [twoSum_bruteForce,twoSum_twoPassHashTable,twoSum_onePassHashTable]
    tests = [
        (([2,7,11,15],9),[0,1]),
        (([3,2,4],6),[1,2]),
        (([3,3],6),[0,1])
    ]
    util.run_tests(solutions,tests)