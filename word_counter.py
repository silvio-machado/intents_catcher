import sys
import os

import operator
chars_to_remove = [
    '”', '“', '–', '\n', '(', ')', '.', ',', '"', "'", ':',
    '?', '!', '-', ';',
]
words_d = []
words = {}
directory_path = os.path.abspath(".")
text_file = None

def file_reader(file_name):
    try:
        with open(f'{directory_path}/{file_name}', 'r') as readed_file:
            return readed_file.readlines()
    except:
        print('File not found.')


def string_converter(text_array):
    correct_len_w = [
        x for x in text_array if len(x)
    ]
    return ' '.join(correct_len_w)


def text_replacer(text, find=['\n'], replace=' '):
    for char in chars_to_remove:
        text = text.replace(char, replace)
    return text


def text_spliter(text, split_condition=None):
    return text.split(split_condition)


if __name__ == '__main__':
    text_file = text_replacer(
            string_converter(file_reader('text.txt'))
        ).lower()
    
    for x in text_spliter(text_file):
        x = x.lower()
        if x not in words and len(x) > 3:
            words[x] = 1
        elif x in words and words[x] >= 1:
            words[x] += 1

    sort_words = sorted(words.items(), key=operator.itemgetter(1))
