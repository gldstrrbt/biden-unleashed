"""Generate clearly synthetic text from a recovered fine-tuned GPT-2 checkpoint."""

import argparse
import csv
import time

import gpt_2_simple as gpt2


def trim_to_sentence(text: str) -> str:
    text = text.replace("...", " ").replace("\n", " ").replace(",", "")
    text = text.replace("<|startoftext|> ", "").strip()
    if not text:
        return text

    if text[-1] in ".!?":
        return text

    last_punctuation = max(text.rfind("."), text.rfind("!"), text.rfind("?"))
    if last_punctuation >= 0:
        return text[: last_punctuation + 1]
    return text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("prefix", help="Prompt prefix for synthetic generation")
    parser.add_argument("--output", default="biden.csv")
    parser.add_argument("--count", type=int, default=1)
    parser.add_argument("--delay", type=float, default=2.0)
    args = parser.parse_args()

    session = gpt2.start_tf_sess()
    gpt2.load_gpt2(session)

    with open(args.output, "a", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        for _ in range(args.count):
            generated = gpt2.generate(
                session,
                length=150,
                temperature=1.5,
                prefix=f"<|startoftext|> {args.prefix}",
                truncate="<|endoftext|>",
                include_prefix=True,
                return_as_list=True,
                nsamples=1,
                batch_size=1,
            )[0]
            text = trim_to_sentence(generated)
            print(text)
            writer.writerow([text])
            time.sleep(args.delay)


if __name__ == "__main__":
    main()