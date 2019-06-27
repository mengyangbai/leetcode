import random
class Codec:
    base62 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    baseurl = 'http://tinyurl.com/'
    tinyTolong = {'1':'1'}
    longTotiny = {}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in Codec.longTotiny:
            return Codec.longTotiny[longUrl]

        shortUrl = '1'
        while shortUrl in Codec.tinyTolong:
            shortUrl = ''.join(random.choice(Codec.base62) for i in range(6))

        shortUrl = Codec.baseurl + shortUrl
        Codec.tinyTolong[shortUrl] = longUrl
        Codec.longTotiny[longUrl] = shortUrl

        return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        longUrl = Codec.tinyTolong[shortUrl]
        return longUrl