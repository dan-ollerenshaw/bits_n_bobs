"""
Quick function to scan for large files in a filesystem.
"""

import os


def list_by_file_size(directory, unit='b'):
    """ Lists files in a directory in descending
        order of size.
        
        Unit param determines the units to print
        (bytes, kilobytes or megabytes).
    """
    assert unit in ('b', 'kb', 'mb'), 'Invalid unit.'

    results = []
    for root, dirs, files in os.walk(directory):        
        for f in files:
            fpath = os.path.join(root, f)

            # catch the case where the file can be listed
            # by os.walk, but not accessed by os.stat
            try:
                obj = os.stat(fpath)
            except FileNotFoundError as err:
                print(f'ERROR: {err}, skipping.')
                continue
            size = obj.st_size
            if unit == 'kb':
                size = round(size / 1024)
            elif unit == 'mb':
                size = round(size / 1048576) 

            to_return = (fpath, size)
            results.append(to_return)

    results = sorted(results, key=lambda x: x[1], reverse=True)
    return results



if __name__ == '__main__':
    print("Import me, don't run me!")
