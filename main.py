import argparse
import os

from src.Recorder import Recorder
from src.EventPlayer import EventPlayer

parser = argparse.ArgumentParser(description='Description of your program')

parser.add_argument(
    '-a', '--action', help='Action type, either "RECORD" or "REPLAY"', required=True)

parser.add_argument(
    '-f', '--filename', help='Filename to replay')

parser.add_argument(
    '-t', '--time', help='Delay time before start of action', default=2)

parser.add_argument(
    '-o', '--overrite', help='if file exists already, overwrite it', default=False, type=bool, nargs='?', const=True)

args = parser.parse_args()

# Check if valid
if not str(args.action).upper() in ["RECORD", "REPLAY"]:
    parser.error('-a needs to be "RECORD" or "REPLAY"')

TIME_DELAY = float(args.time)

# Replay
if str(args.action).upper() == "REPLAY":
    filename = args.filename

    if not filename:
        parser.error('-f no filename passed')

    if "." in filename:
        filename = filename.split(".")[0]

    if not os.path.exists("savedRecordings"):
        os.makedirs("savedRecordings")

    if not os.path.isfile("savedRecordings/"+filename+".txt"):
        parser.error(
            f'-f given file {filename} does not exist in the "savedRecordings" folder')

    EP = EventPlayer()
    EP.startPlaying(filename, TIME_DELAY)


# Record
if str(args.action).upper() == "RECORD":

    filename = args.filename

    if filename:
        if "." in filename:
            filename = filename.split(".")[0]

    overrite=args.overrite

    Rec = Recorder(overrite)
    Rec.startRecording(TIME_DELAY, filename)
