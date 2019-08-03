# try-except-else usage

def count_words(filename):
    """Count the number of words in the given file"""
    try:
        with open(filename) as file_obj:
            content = file_obj.read()

    except FileNotFoundError:
        print('Sorry, the file <' + filename + '> doesn\'t exist.')

    else:
        words = content.split()
        num_words = len(words)
        print('The file', filename, 'has about', str(num_words), 'words.')

if __name__ == "__main__":
    filenames = ['play.py', 'word_count.py', 'not_existed.txt']

    for file in filenames:
        count_words(file)
