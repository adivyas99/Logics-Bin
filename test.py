def solution(A):
    #no=0
    #A = sorted(A)
    A = sorted(list(set(A)))
    st = A[0]
    en = A[-1]
    f=0
    for i in range(st, en+1):
        if i not in A:
            if i>0:
                f=1
                no=i
                break
        if i==en:
            if i>0:
                no=i+1
                f=1
                break
    if f==0:
        return 1
    else: 
        return no
    
    
