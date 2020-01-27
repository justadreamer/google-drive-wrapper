from GoogleDriveWrapper import *
import argparse
from pathlib import Path
from pathlib import PurePath

def get_args():
    parser = argparse.ArgumentParser(description='upload {file} {google_drive_dir}')
    parser.add_argument('remote_path', nargs='?', default='/', type=str, help='path to google drive directory')
    parser.add_argument('local_path', type=str, help='path to the directory to which we downsync the contents of the google drive directory')
    args = parser.parse_args()
    return args

def download(remote_path, local_path):
    google_folder = Folder(remote_path, createIfNotExists=False)
    google_folder.downloadAll(local_path)

def main():
    args = get_args()
    remote_path = args.remote_path
    local_path = args.local_path

    if not Path(local_path).exists(): # we create dir if not exists
        print()
        print(f"path {local_path} does not exist")
        exit(1)
    if not Path(local_path).is_dir():
        print(f"path {local_path} is not a directory")
        exit(1)

    print(f"Downsyncing Google Drive dir: {remote_path} into local: {local_path}")
    wrapped_remote_path = PurePath(remote_path)
    if remote_path == '/':
        wrapped_remote_path = PurePath()
    download(wrapped_remote_path, local_path)


if __name__ == '__main__':
    main()
