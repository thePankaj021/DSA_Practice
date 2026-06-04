class Codec:

    def encode(self, longUrl: str) -> str:
        return longUrl  # simple identity encoding

    def decode(self, shortUrl: str) -> str:
        return shortUrl