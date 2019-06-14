input_text = "hello Hello HELLO hi HI Hi "


def word_finder(text, ignore_case=True):

    word_list = text.split()
    
    words_set = set(word_list)
    return words_set



print(word_finder(input_text))
