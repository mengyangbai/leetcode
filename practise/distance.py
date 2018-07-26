# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S, T):
    # write your code in Python 3.6
    '''
        not the classic Edit Distance problem
        because we can only caluate one time
        no dp needed
    '''
    if S == T:
        return "NOTHING"

    S = list(S)
    T = list(T)
    if len(S) == len(T) + 1:
        # delete
        for j in range(len(T))[::-1]:
            for i in range(len(S))[::-1]:
                if T[j] == S[i]:
                    del S[i]
                    del T[j]
                    break

        if len(T) != 0 or len(S) != 1:
            return "IMPOSSIBLE"
        else:
            return "DELETE {}".format(S[0])

    elif len(S) == len(T) - 1:
        # insert
        for i in range(len(S))[::-1]:
            for j in range(len(T))[::-1]:
                if T[j] == S[i]:
                    del S[i]
                    del T[j]
                    break

        if len(S) != 0 or len(T) != 1:
            return "IMPOSSIBLE"
        else:
            return "INSERT {}".format(T[0])

    elif len(S) == len(T):
        result = []
        for i in range(len(S)):
            if S[i] != T[i]:
                result.append(S[i])

        if len(result) == 2:
            return "SWAP {} {}".format(result[0], result[1])
        else:
            return "IMPOSSIBLE"

    return "IMPOSSIBLE"


print(solution("abc", "cab"))
