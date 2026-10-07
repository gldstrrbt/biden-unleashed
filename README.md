# Biden Unleashed

Recovered 2020 generative-media / satire experiment.

The project explored training a GPT-2 language model on a corpus assembled from public Joe Biden speeches and interviews, alongside a separately prepared collection of segmented audio clips and transcripts. The surviving code covers transcript/audio metadata preparation, GPT-2 fine-tuning, and synthetic text generation.

This repository is preserved as historical experimental code. Generated text is synthetic and should not be represented as an authentic quotation or statement by Joe Biden or any other real person.

## What survived

- `src/format_transcripts.py` — converts per-source transcript text into pipe-delimited filename/text metadata suitable for pairing transcript lines with numbered audio clips.
- `src/train_biden.py` — fine-tunes the 355M GPT-2 model with `gpt-2-simple` using the recovered training corpus workflow.
- `src/generate_biden.py` — loads a fine-tuned checkpoint and generates synthetic text from a caller-supplied prefix.
- `DATASET_NOTES.md` — inventory of the recovered audio/transcript material without republishing the media or full transcript corpus.

## Historical environment

The original project used `gpt-2-simple` 0.7.1 and its TensorFlow 1.x-era stack. Modern Python/TensorFlow installations are unlikely to run this unchanged.

The original training script selected the GPT-2 `355M` model and requested up to 100,000 fine-tuning steps. Those values are preserved as defaults in the recovered script.

## Archive cleanup

The recovered ZIP also contained:

- hundreds of WAV speech clips;
- full/compiled speech and interview transcript corpora;
- duplicate copies of one 25-clip source set;
- an upstream `gpt-2-simple` README, license, setup script and package metadata;
- a Tiny Shakespeare sample corpus;
- an earlier one-off generation test that duplicated the final generation workflow.

Those items are not committed here. The archive keeps the project-specific source while avoiding large media, duplicated material, and vendored third-party files.

## Recovered runtime / iClone batch

A second recovered project folder adds evidence of the later live-media pipeline. It includes:

- `src/iclone/load_audio_viseme.py` — cleaned iClone Python proof-of-concept that loads an audio file onto the first avatar and invokes the avatar's viseme/lip-sync component.
- `archive/aitextgen/rev_transcript_scraper.py` — historical Selenium-based transcript collection / cleanup script used while building Biden text corpora.
- `archive/aitextgen/custom_tokenizer_train.py` — recovered custom-tokenizer training experiment from a later `aitextgen` phase.
- Additional cleaned generation and Colab/GPU training experiments were recovered from this batch, but are not committed in this archive snapshot.
- `RUNTIME_NOTES.md` — reconstructed deployment history that clearly separates remembered two-computer/Twitch architecture from source that has actually been recovered.
- `ASSET_NOTES.md` — inventory of large iClone/Character Creator project assets and test media intentionally left out of GitHub.

This batch does **not** contain the Twitch input listener, network handoff, second-machine playback watcher, unattended restart tooling, or trained model checkpoints. Those remain recovery targets if the older machine/drive/SD-card material turns up later.
