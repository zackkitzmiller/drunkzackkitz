def file_to_words(filename):
    open_file = open(filename)
    open_file.seek(0)
    data = open_file.read()
    words = data.split()
    return words
