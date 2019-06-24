import math
class Solution:
    def minimizeError(self, prices: [str], target: int) -> str:
        diff = []
        low, high = 0, 0
        for _, p in enumerate(map(float, prices)):
            f, c = math.floor(p), math.ceil(p)
            low, high = low + f, high + c
            fDiff, cDiff = p - f, c - p
            diff.append((fDiff - cDiff, fDiff, cDiff))
        if not low <= target <= high:
            return "-1"
        ceilN = target - low
        diff = sorted(diff, reverse=True)
        return "{:.3f}".format(sum([d[2] for d in diff[:ceilN]]) + sum([d[1] for d in diff[ceilN:]]))


class BetterSolution:
    def minimizeError(self, prices: [str], target: int) -> str:
        base = 0
        remainders = []

        for price in prices:
            integer, remainder = price.split(".")
            base += int(integer)
            if remainder != "000":
                remainders.append(int(remainder))

        if target < base or target > base + len(remainders):
            return "-1"

        remainders.sort(reverse=True)
        result = 0
        i = 0

        while i < len(remainders) and base + i < target:
            result += 1000 - remainders[i]
            i += 1

        result += sum(remainders[i:])
        return "{:.3f}".format(result / 1000)