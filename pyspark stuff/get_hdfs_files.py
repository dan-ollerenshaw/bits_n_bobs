"""
Extract filenames from HDFS.
"""

import subprocess


def get_hdfs_files(directory,
                   recursive=False,
                   strings_to_search_for=[''],
                   decoder='utf-8'):
    """ Use a terminal command in python to get equivalent
        of os.listdir() from HDFS.

        Recursive kwarg will ad -R and search all subdirectories.

        If strings_to_search_for is specified, it will return
        only files that contain all those strings.
        (e.g. [".csv"])

        #XXX could add kwarg for any instead of all...
    """

    command = f"hdfs dfs -ls -C -R {directory}" if recursive\
              else f"hdfs dfs -ls -C {directory}"

    p = subprocess.Popen(command,
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)

    files = [path.decode(decoder).rstrip('\n') for path in p.stdout.readlines()]
    matching_files = [f for f in files\
                      if all(
                        [s.lower() in f.lower() for s in strings_to_search_for]
                        )
                      ]

    return matching_files


if __name__ == '__main__':
    print("Import me, don't run me!")
