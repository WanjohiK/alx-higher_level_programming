#!/usr/bin/python3
"""
5-text_indentation Module
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters:
    '.', '?' and ':'

    Args:
        text: string input
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    split_sentence_list = list()
    new_sentence = list()
    letters_list = list()

    for char in text:
        letters_list.append(char)
        if char in ['.', '?', ':']:
            split_sentence_list.append(''.join(letters_list))
            letters_list.clear()

    if letters_list:
        split_sentence_list.append("".join(letters_list))
    letters_list.clear()

    for sentence in split_sentence_list:
        new_sentence.append(sentence.strip(' '))
    split_sentence_list.clear()

    for char in new_sentence[-1]:
        if char in ['.', '?', ':']:
            print("\n\n".join(new_sentence))
            print()
            return

    print("\n\n".join(new_sentence), end='')
