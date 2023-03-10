#https://www.codewars.com/kata/52b7ed099cdc285c300001cd
def sum_of_intervals(intervals):
    intervals = [list(i) for i in intervals]
    intervals = sorted(intervals)
    temp = intervals[0][0]
    for i in range(1, len(intervals)):
        if intervals[i][0]<intervals[i-1][1] or (intervals[i][0]>=intervals[i-1][1] and intervals[i][0]<temp):
            temp = max(temp, intervals[i-1][1])
            intervals[i-1][1] = intervals[i][0]
        else:
            intervals[i-1][1] = max(temp, intervals[i-1][1])
        if intervals[-1] == intervals[i]:
            intervals[i][1]=max(temp, intervals[i][1])
    len_intervals = 0
    for i in intervals:
        len_intervals = len_intervals + i[1] - i[0]
    return len_intervals
