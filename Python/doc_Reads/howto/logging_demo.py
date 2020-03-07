import logging

# basic workflow
def do_opeartion():
    # Some operations here
    logging.info('do operations.')
    logging.warning('Watch out!')
    logging.info('Told ya!')
    logging.error('This is an error msg.')

def main():
    logging.basicConfig(filename='myapp.log', filemode='a', level=logging.DEBUG)
    logging.info('Start executing main()')
    do_opeartion()
    logging.info('Finish executing main()')

if __name__ == "__main__":
    main()