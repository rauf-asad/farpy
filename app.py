import click
import os
from farpy.application import inplace_replace

@click.command()
@click.option('--path', type=str, help='file or folder path')
@click.option('--filetype', type=str, help='filetypes to change')
@click.option('--old', type=str, help='string to replace')
@click.option('--new', type=str, help='string to replace with')
def main(path, filetype, old, new):
    if os.path.isfile(path):
        if filetype:
            if path.endswith(f'.{filetype}'):
                inplace_replace(path, old, new)
    if os.path.isdir(path):
        for dirs, subs, files in os.walk(path):
            for file in files:
                if file.endswith(f'.{filetype}'):
                    inplace_replace(os.path.join(path, dirs, file), old, new)


if __name__ == '__main__':
    main()
