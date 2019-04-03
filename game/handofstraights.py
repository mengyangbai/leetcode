class Solution:
    def isNStraightHand(self, hand: [int], W: int) -> bool:
        counts = [0]*W
        for card in hand:
            counts[card % W] += 1
        return all(c == counts[0] for c in counts)

import collections
class MySolution:
    def isNStraightHand(self, hand, W):
        c = collections.Counter(hand)
        for i in sorted(c):
            if c[i] > 0:
                for j in range(W)[::-1]:
                    c[i + j] -= c[i]
                    if c[i + j] < 0:
                        return False
        return True

a = Solution()
print(a.isNStraightHand([5,1],1))

'''
    public boolean isNStraightHand(int[] hand, int W) {
        Map<Integer, Integer> c = new TreeMap<>();
        for (int i : hand) c.put(i, c.getOrDefault(i, 0)+1);
        for (int it : c.keySet())
            if (c.get(it) > 0)
                for (int i = W - 1; i >= 0; --i) {
                    if (c.getOrDefault(it + i, 0) < c.get(it)) return false;
                    c.put(it + i, c.get(it + i) - c.get(it));
                }
        return true;
    }
'''