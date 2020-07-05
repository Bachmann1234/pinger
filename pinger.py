from playsound import playsound
from time import sleep
import sys
import argparse
import os

ERASE_IN_LINE_TERM_ESCAPE = "\033[K"
TONE_SOUND = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tone.wav")


def print_replaceable_message(msg):
    sys.stdout.write(ERASE_IN_LINE_TERM_ESCAPE)
    print("\t" + msg, end="\r")


def countdown(seconds):
    for tick in range(seconds):
        print_replaceable_message(str(seconds - tick))
        sleep(1)


def main(initial_delay, time_between_pongs):
    try:
        countdown(initial_delay)
        while True:
            countdown(time_between_pongs)
            print_replaceable_message("DING!")
            playsound(TONE_SOUND)
    except KeyboardInterrupt:
        sys.stdout.write(ERASE_IN_LINE_TERM_ESCAPE)
        print("\b\bGoodbye!")


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--initial_delay", "-i", type=int, default=0)
    parser.add_argument("--time_between_pongs", "-t", type=int, default=4)
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    main(args.initial_delay, args.time_between_pongs)
