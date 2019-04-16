"""
Write an equivalent of os.listdir() for a HDFS setting.

N.B.: the API for subprocess changes a lot, this is for python3.6
It's a little simpler for python3.7 with the capture_output option.
"""

import subprocess


def get_hdfs_files(directory: str,
                   recursive: bool = False,
                   decoder='utf-8') -> list:
    """ Use a terminal command to get equivalent of os.listdir()
        from HDFS.

        Recursive kwarg will also search all subdirectories.
    """
    # define the command
    command = ['hdfs',
               'dfs',
               '-ls',
               '-C' # XXX can't find documentation on this option
               ]

    if recursive:
        command.append('-R')

    command.append(directory)

    # run the command
    output = subprocess.run(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)

    # raise an err if we get any errors (e.g. invalid directory)
    if output.returncode != 0:
        raise Exception(f'{output.stderr.decode(decoder)}')

    files = output.stdout.decode(decoder).split('\n')

    return files



if __name__ == '__main__':
    print("Import me, don't run me!")

