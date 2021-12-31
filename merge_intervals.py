def merge(intervals):
    intervals.sort(key=lambda x:x[0])
    #if (0,2),(2,3) then (0,3) is appended in merge else (0,7)(4,5) then (0,5)(4,7) then (0,7)
    merge=[]
    for i in intervals:
        if (len(merge)==0) or (merge[-1][1]<i[0]):
            merge.append(i)
        else:
            merge[-1][1]=max(i[1],merge[-1][1])
    return merge
print(merge([[0,4],[3,7]]))