# set1 = set(["Geeks", "For", "Geeks"])
# print("\nSet with the use of List: ")
# print(set1)
# a = list(list())
# a.append([12,13])
# a.append([11,12])
# a = sorted(a)
# print(a)
# print(a[-1][0])
def merge(intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)
        n = len(intervals)
        ans = list(list())
        for i in range(0,n):
            if len(ans) == 0 or intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1],intervals[i][1])
        return ans

print(merge([[1,3],[2,6],[8,10],[15,18]]))