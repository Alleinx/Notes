# Consider Generator when need to process a seqeuence and return result.

def index_words_list(text):
    '''
    Iter Version
    '''
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

def index_words_gen(text):
    '''
    Generator version,
    beware that each geneator can be used only once;
    If need to store the result, make sure to convert generator into list/array
    '''
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

address = 'Four score and seven years ago...'
result = index_words_list(address)
print(result)

result = index_words_gen(address)
# Store the result if needed.
# store = list(result)
print(result)
# When need to use it:
for item in result:
    print(item)
