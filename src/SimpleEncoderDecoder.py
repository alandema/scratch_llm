from EncoderDecoderBase import EncoderDecoderBase
import torch


class SimpleEncoderDecoder(EncoderDecoderBase):
    def __init__(self, data: str):
        super().__init__(data)

    def tokenize(self):
        return sorted(list(set(self.data)))

    def create_token_map(self):
        token_map = {ch: i for i, ch in enumerate(self._tokens)}
        r_token_map = {i: ch for i, ch in enumerate(self._tokens)}
        return token_map, r_token_map

    def encode(self, text):
        return torch.tensor([self.token_map[ch] for ch in text], dtype=torch.long)

    def decode(self, encoded):
        return ''.join([self.r_token_map[i] for i in encoded.tolist()])


if __name__ == "__main__":

    with open('.\\data\\text.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    tk = SimpleEncoderDecoder(text)

    encoded = tk.encode('hii there')
    print(encoded)

    decoded = tk.decode(encoded)
    print(decoded)
