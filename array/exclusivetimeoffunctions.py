class Solution:
    def exclusiveTime(self, n: int, logs: [str]) -> [int]:
        res = [0 for _ in range(n)]

        stack = []
        for log in logs:
            fn, typ, time = log.split(':')
            fn, time = int(fn), int(time)

            if typ == 'start':
                if stack:
                    res[stack[-1]] += time - prev_time 
                stack.append(fn)
                prev_time = time
            else:
                res[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return res

a = Solution()
a.exclusiveTime(2,
["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"])