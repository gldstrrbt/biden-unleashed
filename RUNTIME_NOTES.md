# Runtime / deployment notes

This recovery batch fills in part of the later **Biden Unleashed** live-media pipeline, but not the complete Twitch deployment.

## Recalled live architecture

The creator recalls running the project across two computers so one machine did not have to handle every GPU-, memory-, and media-heavy task at once:

1. **Generation / input machine**
   - received live input from Twitch;
   - ran text-generation and related processing;
   - produced generated text/audio artifacts;
   - made those artifacts available across the home network.

2. **Playback / streaming machine**
   - watched for newly generated artifacts;
   - played/rendered the corresponding media;
   - streamed the resulting output to Twitch.

The home network included a modified/open-source-router setup and remote administration so the machines could be recovered while unattended. The creator recalls using SSH and a network-connected power strip when the computers froze, with both machines configured to boot and restart the required scripts automatically.

The exact router firmware, network topology, remote-recovery scripts, Twitch listener, file-transfer mechanism, second-machine watcher/player, and power-strip automation are **not present in the recovered files**. They should be treated as unrecovered project history rather than reconstructed source.

## What this batch actually contains

The surviving source in `biden_unleashed_01.zip` is concentrated in two areas:

- **aitextgen experiments**: transcript scraping, custom tokenization, model training, and generation tests from a later PyTorch/aitextgen phase of the project.
- **iClone experiments**: Reallusion iClone Python tests for loading generated audio onto an avatar and invoking its viseme/lip-sync component.

The ZIP also contained large Reallusion project/avatar files, test WAV/MP3 files, transcript/model corpora, a browser driver, and vendored `aitextgen` package documentation/setup material. Those are intentionally omitted from the GitHub code archive.

## Missing artifacts worth recovering later

If older disks, SD cards, or computers turn up, useful search targets include:

- Twitch chat / IRC listener code;
- generated-text-to-speech or voice-cloning handoff code;
- network file-transfer / shared-folder / polling code;
- the playback-machine watcher and media player / streamer scripts;
- OBS or streaming configuration;
- startup scripts / scheduled tasks used for unattended reboot recovery;
- SSH or router automation scripts;
- network-power-strip control code;
- trained model checkpoints and tokenizer/config directories;
- screenshots, clips, or Twitch correspondence documenting the live deployment.

The creator recalls that the stream eventually received Twitch partnership, but that status is not independently documented by the source recovered so far. If an email, dashboard screenshot, or other record is found later, it would be useful supporting archival material.