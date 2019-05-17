import sys
import os

from pydub import AudioSegment
from pydub.playback import play


def Convert(mixedFile, cleanFile, outFile):
    mixed_path = mixedFile
    clean_path = cleanFile

    mixed_audio = AudioSegment.from_file(mixed_path, format="wav")
    clean_audio = AudioSegment.from_file(clean_path, format="wav")
    
    if mixed_audio.duration_seconds < 2.0:
        paddingSeconds = 2.1 - mixed_audio.duration_seconds
        silence = AudioSegment.silent(duration=int(paddingSeconds * 1000), frame_rate=mixed_audio.frame_rate)

        mixed_audio = mixed_audio + silence
        clean_audio = clean_audio + silence
        mixed_audio.export(mixedFile, format="wav")
        clean_audio.export(cleanFile, format="wav")

    clean_audio_invert = clean_audio.invert_phase()
    noise_audio = mixed_audio.overlay(clean_audio_invert)

    noise_audio.export(outFile, format="wav")
        
