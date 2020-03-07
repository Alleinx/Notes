import logging

# basic workflow


def do_opeartion():
    # Some operations here
    logging.info('do operations.')

    # logging.warning(), when you want some warning
    logging.warning('Watch out!')

    # when meet a RuntimeError
    # can also use logging.exception(), logging.critical()
    logging.error('This is an error msg.')

    logging.exception('This is a exception msg.', exc_info=False)
    logging.critical('This is a critical msg.')


def main():
    # Config the log
    # filename: save log information into file.
    # filemode: 'w', 'a', ...
    # format: change the format of logging msg.
    # level : threshold, indicates what types of info can be printed out.

    logging.basicConfig(filename='./myapp.log', filemode='a',
                        format='[%(asctime)s] %(levelname)s: %(message)s', level=logging.DEBUG)

    # logging.info(), normal record
    logging.info('Start executing main()')
    # can also use logging.debug for logging.info() alternative.
    logging.debug('This is a debug msg.')

    do_opeartion()
    logging.info('Finish executing main()')


if __name__ == "__main__":
    main()
