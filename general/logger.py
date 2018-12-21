""" Bog standard config for logging.
"""

import os
import logging


def logger(name,
           output_type='stdout',
           filename='test.log'):
    """ Example use:

        from logger import logger

        LOGGER = logger('some_name', output_type='stdout')
        LOGGER.info('hello world!')
    """

    assert output_type in ('file', 'stdout')

    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)

    if output_type == 'file':
        handler = logging.FileHandler(filename)
    else:
        handler = logging.StreamHandler(os.sys.stdout)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')

    handler.setFormatter(formatter)
    # before we add the handler, remove any existing ones
    # I'm assuming that this is the behaviour we want 99% of the time
    log.handlers = []
    log.addHandler(handler)

    return log


if __name__ == '__main__':
    print("Import me, don't run me!")
