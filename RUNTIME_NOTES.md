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

The home network ran through a router flashed with **DD-WRT**, chosen for the extra control it gave over the local network and remote administration. That made it easier to reach and recover the setup from elsewhere, but it could not solve unreliable consumer internet or the other failure points in the two-machine pipeline.

Remote recovery also included SSH / remote access, a network-connected power strip, and machines configured to boot and relaunch pieces of the system automatically after a reset.

The exact network topology, remote-recovery scripts, Twitch listener, file-transfer mechanism, second-machine watcher/player, and power-strip automation are **not present in the recovered files**. They should be treated as unrecovered project history rather than reconstructed source.

## Why the live stream stopped

The stream eventually reached Twitch Partner status, but keeping an always-on setup alive became increasingly unrealistic during peak COVID.

The creator was avoiding the subway before vaccines and splitting time between Queens and a partner's home, at times walking roughly seven miles each way. A frozen machine, memory problem, or bad connection could take the stream down for days if the problem could not be solved remotely.

DD-WRT and the remote-reset setup helped, but they could not remove the underlying logistical problem: two temperamental machines, unreliable connections, and a homemade 24/7 media pipeline still needed physical attention sometimes.

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