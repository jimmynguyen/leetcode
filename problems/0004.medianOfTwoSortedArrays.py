# https://leetcode.com/problems/median-of-two-sorted-arrays/
import math
import util


def medianOfTwoSortedArrays(nums1,nums2):
    m,n = len(nums1),len(nums2)
    o = m+n
    if o == 1:
        return (nums1 + nums2)[0]
    i,j = 0,0
    while i+j < math.ceil(o/2.0)-1:
        if j >= n or (i < m and nums1[i] <= nums2[j]):
            i += 1
        else:
            j += 1
    if i >= m:
        a,b = nums2[j],nums2[j+1]
    elif j >= n:
        a,b = nums1[i],nums1[i+1]
    else:
        a = min(nums1[i],nums2[j])
        if a == nums1[i]:
            if i < m-1:
                b = min(nums1[i+1],nums2[j])
            else:
                b = nums2[j]
        elif a == nums2[j]:
            if j < n-1:
                b = min(nums1[i],nums2[j+1])
            else:
                b = nums1[i]
    if o%2 == 1:
        return min(a,b)
    else:
        return (a+b)/2.0


if __name__ == "__main__":
    solutions = [medianOfTwoSortedArrays]
    tests = [
        (([1,3],[2]),2),
        (([1,2],[3,4]),2.5),
        (([0,0],[0,0]),0),
        (([],[1]),1),
        (([2],[]),2)
    ]
    util.run_tests(solutions,tests)