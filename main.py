import os
import sys
import mido
from mido import MidiFile
from moviepy import *
import time


args = sys.argv

# 引数が足りない場合
if len(args) < 3:
    print("Usage: python main.py <MIDI FilePath> <Source Video FilePath>")
    sys.exit()

MIDI_FILE = args[1]
SOURCE_VIDEO = args[2]

print(f"midi: {MIDI_FILE}")
print(f"video: {SOURCE_VIDEO}")


# ファイルの存在確認
if os.path.isfile(MIDI_FILE) == False:
    print("MIDIファイルが存在しません")
    sys.exit()

if os.path.isfile(SOURCE_VIDEO) == False:
    print("動画ファイルが存在しません")
    sys.exit()


mid = MidiFile(MIDI_FILE)
print(f"MIDI Type: {mid.type}")

print(f"Playback time: {mid.length} sec")
# print(f"Tracks: {mid.print_tracks}")

ports = mido.get_output_names()
print(ports)


with mido.open_output(ports[0]) as outport:
    for msg in mid:
        time.sleep(msg.time)
        if not msg.is_meta:
            print(outport, msg)
            outport.send(msg)
