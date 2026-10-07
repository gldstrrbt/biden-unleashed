"""Historical GPT-2 fine-tuning entry point for the Biden Unleashed experiment."""

import argparse
import os

import gpt_2_simple as gpt2


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("training_file", nargs="?", default="joe_marlarky_mod.txt")
    parser.add_argument("--model", default="355M")
    parser.add_argument("--steps", type=int, default=100000)
    args = parser.parse_args()

    if not os.path.isdir(os.path.join("models", args.model)):
        print(f"Downloading {args.model} model...")
        gpt2.download_gpt2(model_name=args.model)

    session = gpt2.start_tf_sess()
    gpt2.finetune(
        session,
        args.training_file,
        model_name=args.model,
        steps=args.steps,
    )
    gpt2.generate(session)


if __name__ == "__main__":
    main()