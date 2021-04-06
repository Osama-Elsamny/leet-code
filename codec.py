class Codec:
    def __init__(self):
        self.map = {}
        self.counter = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.counter += 1
        short_url = 'http://tinyurl.com/{}'.format(self.counter)
        self.map[short_url] = longUrl
        return short_url

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.map[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
