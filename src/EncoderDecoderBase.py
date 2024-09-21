
class EncoderDecoderBase(object):
    def __init__(self, data):
        self.data = data

        self._tokens = self.tokenize()
        self._token_map, self._r_token_map = self.create_token_map()

    def tokenize(self):
        # Implement method in child class
        pass

    def create_token_map(self):
        # Implement method in child class
        pass

    @property
    def tokens(self):
        return self._tokens

    @tokens.getter
    def tokens(self):
        return self._tokens

    @property
    def token_map(self):
        return self._token_map

    @token_map.getter
    def token_map(self):
        return self._token_map

    @property
    def r_token_map(self):
        return self._r_token_map

    @r_token_map.getter
    def r_token_map(self):
        return self._r_token_map


if __name__ == "__main__":
    print(EncoderDecoderBase("hello worldsss"))
