class Codec:
    def encode(self, strs):
        res = []
        for s in strs:
            res.append(s.replace(':', '::')+':;')
        return ''.join(res)

    def decode(self, s):
        res = []
        i, n, tmp = 0, len(s), ''
        while i < n:
            if s[i] == ':' and i+1 < n and s[i+1] == ';':
                res.append(tmp)
                i += 2
                tmp = ''
            elif s[i] == ':' and i+1 < n and s[i+1] == ':':
                tmp += ':'
                i += 2
            else:
                tmp += s[i]
                i += 1
        if tmp:
            res.append(tmp)
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
