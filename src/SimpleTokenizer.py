from TokenizerBase import TokenizerBase


class SimpleTokenizer(TokenizerBase):
    def __init__(self, data: str):
        super().__init__(data)

        self.tokens = self.tokenize()
        self.token_map, self.r_token_map = self.create_token_map()

    def tokenize(self):
        tokens = sorted(list(set(self.data)))
        return tokens

    def create_token_map(self):
        token_map = {ch: i for i, ch in enumerate(self.tokens)}
        r_token_map = {i: ch for i, ch in enumerate(self.tokens)}
        return token_map, r_token_map

    def encode(self, text):
        return [self.token_map[ch] for ch in text]

    def decode(self, encoded):
        return ''.join([self.r_token_map[i] for i in encoded])


if __name__ == "__main__":

    with open('src\\data\\text.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    tk = SimpleTokenizer(text)

    encoded = tk.encode('hii there')
    print(encoded)

    decoded = tk.decode(encoded)
    print(decoded)
