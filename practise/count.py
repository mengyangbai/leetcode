def solution(M, A):
    N = len(A)
    count = [0] * (M + 1)
    maxOccurence = 0
    index = -1
    for i in range(N):
        if count[A[i]] > 0:
            tmp = count[A[i]] + 1
            if tmp > maxOccurence:
                maxOccurence = tmp
                index = i
            count[A[i]] = tmp
        else:
            count[A[i]] = 1
    return A[index]


A = [0, 5, 5, 5, 5, 5, 9, 9, 9, 9, 9, 9]

print(solution(9, A))
