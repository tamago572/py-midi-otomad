import os
import sys
import mido


args = sys.argv

if len(args) < 3:
    print("Usage: python main.py <MIDI FilePath> <Source Video FilePath>")
    sys.exit()

MIDI_FILE = args[1]
SOURCE_VIDEO = args[2]

print(f"midi: {MIDI_FILE}")
print(f"video: {SOURCE_VIDEO}")

