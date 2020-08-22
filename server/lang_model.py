#!/usr/bin/env python
# coding: utf-8
from difflib import SequenceMatcher


dictionary = {
        "инет": "Интернет",
        "ЛСник": "лицевой счёт",
        "абонплата": "абонентская плата"
    }


def handletext(text):
    words = text.split()
    wordpairs = [words[i]+' '+words[i+1] for i in range(len(words)-1)]
    for phrase in wordpairs:
        for key in dictionary.keys():
            if SequenceMatcher(a=phrase.lower(), b=key.lower()).ratio() > 0.85:
                text = text.replace(phrase, dictionary[key])
    for phrase in words:
        for key in dictionary.keys():
            if SequenceMatcher(a=phrase.lower(), b=key.lower()).ratio() > 0.85:
                text = text.replace(phrase, dictionary[key])
    return text
