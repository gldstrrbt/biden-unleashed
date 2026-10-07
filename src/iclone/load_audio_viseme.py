"""Historical iClone lip-sync proof of concept for Biden Unleashed.

Run inside iClone's Python environment with an avatar already loaded.
"""

import os
import RLPy


def load_vocal(audio_path="2.wav", clip_name="Default"):
    """Load an audio file onto the first avatar and generate viseme timing."""
    avatars = RLPy.RScene.GetAvatars()
    if not avatars:
        raise RuntimeError("No avatar is loaded in the current iClone scene")

    avatar = avatars[0]
    viseme_component = avatar.GetVisemeComponent()
    audio = RLPy.RAudio.CreateAudioObject()
    start_time = RLPy.RGlobal.GetTime()

    if not os.path.exists(audio_path):
        raise FileNotFoundError(audio_path)

    RLPy.RAudio.LoadAudioToObject(avatar, audio_path, start_time)
    return viseme_component.LoadVocal(audio, start_time, clip_name)


if __name__ == "__main__":
    print(load_vocal())