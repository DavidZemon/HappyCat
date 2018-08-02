#!/usr/bin/python3
import os
import subprocess
import sys


SOUND_BYTES = [
    ['Happy', 'meow_mix.mp3'],
    ['Angry', 'angry_cat.mp3'],
    ['Intimidating', 'lion.mp3'],
    ['Lonely', 'lonely.mp3']
]


def play(file_path: str) -> None:
    if os.path.exists(file_path):
        subprocess.check_output(['mpg123', file_path], stderr=subprocess.PIPE)
    else:
        print('Not implemented yet :\'(', file=sys.stderr)


def run() -> None:
    while True:
        prompt = 'Choose your emotion:' + os.linesep
        for i in range(len(SOUND_BYTES)):
            prompt += '    {0}: {1}{2}'.format(i + 1, SOUND_BYTES[i][0], os.linesep)
        prompt += '    q: Quit' + os.linesep
        answer = input(prompt).strip()

        if 'q' == answer:
            return
        else:
            # noinspection PyBroadException
            try:
                answer = int(answer)
                if answer in range(1, len(SOUND_BYTES) + 1):
                    play(SOUND_BYTES[answer - 1][1])
                else:
                    print('Select a number 1-{}'.format(len(SOUND_BYTES)))
            except:
                print('Select a number 1-{}'.format(len(SOUND_BYTES)))


if '__main__' == __name__:
    run()
