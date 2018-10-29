"""Pig Latin

Pig Latin is an argot ("secret" language) in which words in English are altered to conceal the words
from others not familiar with the rules.

You convert a word to pig latin by transferring the initial consonant or consonant cluster of the word
to the end of the word with -ay appended to the end. If the word starts with a vowel (including y),
append -yay to the end. For example, "pig" would become igpay (taking the 'p' and 'ay' to create a suffix).

Examples:
Input: say  Output: aysay

Input: english  Output: englishyay

Input: smile  Output: ilesmay

Write a program that translates the user input (an English word) to Pig Latin.

By: Dick STADA, NL
October 2018
Comments are welcome!
"""
import re


def get_string_from_user():
    sentence = input("Give a sentence or word: ").strip()
    sentence = re.sub(' +', ' ', sentence)  # delete multiple spaces
    return sentence


def translate_to_pig_latin(sentence):
    vowels = ["a", "o", "e", "i", "u", "y"]
    sent_lst = sentence.lower().split(" ")    # Split in separate words and make all chars lower
    translation = ""
    for w in sent_lst:  # word for word
        if w[0] not in vowels:  # Word starts with consonant.
            for l in w:
                if l in vowels:
                    w.index(l)       # Position of the vowel l in the word w
                    break
            translation += " " + w[w.index(l):] + w[:w.index(l)] + "ay"
        else:   # Word starts with vowel
            if w[len(w)-1] in vowels:
                w = w + "way"
            else:
                w = w + "ay"
            translation += " " + w
    return translation


def print_translation(translation):
    print(translation)


def main():
    sentence = get_string_from_user()
    translation = translate_to_pig_latin(sentence)
    print_translation(translation)


if __name__ == "__main__":
    main()
