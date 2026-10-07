"""Recovered custom-tokenizer training experiment using aitextgen."""

from aitextgen.TokenDataset import TokenDataset
from aitextgen.tokenizers import train_tokenizer
from aitextgen import aitextgen

FILE_NAME = "joe.txt"
VOCAB_FILE = "aitextgen-vocab.json"
MERGES_FILE = "aitextgen-merges.txt"


def main():
    train_tokenizer(FILE_NAME)
    ai = aitextgen(
        model="trained_model/pytorch_model.bin",
        vocab_file=VOCAB_FILE,
        merges_file=MERGES_FILE,
        config="trained_model/config.json",
    )
    data = TokenDataset(
        FILE_NAME,
        vocab_file=VOCAB_FILE,
        merges_file=MERGES_FILE,
        block_size=64,
    )
    ai.train(data, batch_size=16, num_steps=1_000_000, line_by_line=False)
    ai.generate(n=2, max_length=1000, temperature=1.5)


if __name__ == "__main__":
    main()