import sys
import os
import subprocess
import argparse

description = 'A quick and dirty way to create a living youtube playlist downloader'

def main():
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-p','--path of Playlist.txt',
        help='Path of Playlist.txt file and folder', required=True)
    args = vars(parser.parse_args())
    plist_path = os.path.abspath(args['path of Playlist.txt'])
    playlist = open(plist_path,'r')
    for line in playlist.readlines():
          subprocess.call(['youtube-dl', line])

if __name__ == '__main__':
    main()
