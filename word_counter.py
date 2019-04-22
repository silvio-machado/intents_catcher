import sys
import os

words = {}
directory_path = os.path.abspath(".")
text_file = None

def file_reader(file_name):
    try:
        with open(f'{directory_path}/{file_name}', 'r')as readed_file:
            return readed_file.readlines()
    except:
        print('File not found.')


def string_converter(text_array):
    return ''.join(text_array)


def text_replacer(text, find, replace):
    return text.replace(find, replace)

def text_spliter(text, split_condition=None):
    return text.split(split_condition)

# with open('text.txt', 'r') as readed_file:
#     text_file = file_reader('text.txt')
#     text_file = [x for x in text_file if x is not '\n']
#     text_file = ''.join(text_file)
#     text_replacer()

if __name__ == '__main__':
    text_file = text_spliter(
        text_replacer(
            string_converter(file_reader('text.txt')),
            '\n',
            ' '
        )
    )

    for x in text_file:
        x = x.lower()
        if x not in words and len(x) > 2:
            words[x] = 1
        elif x in words and words[x] >= 1:
            words[x] += 1
