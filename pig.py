"""Pig Latin

Pig Latin is an argot ("secret" language) in which words in English are altered to conceal the words
from others not familiar with the rules.

You convert a word to pig latin by transferring the initial consonant or consonant cluster of the word
to the end of the word with -ay appended to the end. If the word starts with a vowel (including y),
append -yay to the end. For example, "pig" would become igpay (taking the 'p' and 'ay' to create a suffix).

Examples:
Input: say
Output: aysay

Input: english
Output: englishyay

Input: smile
Output: ilesmay

Write a program that translates the user input (an English word) to Pig Latin.

By: Dick STADA, NL
October 2018
Comments are welcome!
"""


def get_string_from_user():
    sentence = input("Give a sentence or word: ")
    return sentence


def translate_to_pig_latin(sentence):
    print(sentence)
    sent = sentence.split(" ")
    print(sent)
    # return translation


def print_translation(translation):
    print(translation)


def main():
    sentence = get_string_from_user()
    translate_to_pig_latin(sentence)
    # print_translation()


main()
