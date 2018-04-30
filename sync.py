from GoogleDriveWrapper import *
import argparse
import sys
from pathlib import Path, PurePath


def parse_path():
    parser = argparse.ArgumentParser(description='sync path to google drive')
    parser.add_argument('path', metavar='path', type=str, help='path to the directory to be synced')
    args = parser.parse_args()
    return Path(args.path).absolute()


def sync(root: Path, path: Path, google_folder=None):
    google_path = path.relative_to(root)
    print(google_path)
    if path.is_dir():
        google_folder = Folder(google_path, createIfNotExists=True)
        for child in path.iterdir():
            sync(root, child,google_folder=google_folder)
    elif path.is_file():
        if google_folder is None:
            dir = path.parent
            google_path = dir.relative_to(root)
            google_folder = Folder(google_path, createIfNotExists=True)
        google_folder.upload(path)


def main():
    path = parse_path()

    if not path.exists():
        print(f"path {path} does not exist")
        exit(1)

    root = path.parent

    print(f"syncing, root: {root}, path: {path}")

    sync(root, path)


if __name__ == '__main__':
    main()
