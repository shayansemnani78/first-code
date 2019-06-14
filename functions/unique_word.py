input_text = "hello python programmers we are programming in python how are you?"


def word_finder(text):
    word_list = text.split()
    words_set = set(word_list)
    return words_set



print(word_finder(input_text))
