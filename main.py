from __future__ import unicode_literals, print_function, division
from io import open
import unicodedata
import string
import re
import random

import torch
import torch.nn as nn
from torch import optim
import torch.nn.functional as F

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

from lang import Lang

def unicode_to_ascii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    )

def normalize_string(s):
    s = unicode_to_ascii(s.lower().strip())
    s = re.sub(r"([.!?])", r"\1", s)
    s = re.sub(r"[^a-zA-Z.!?]+", r"", s)
    return s

def read_data(lang_1, lang_2, reversed=False):
    print("importing dataset")
    with open("data/{}-{}.txt".format(lang_2, lang_1), "r", encoding="utf-8").read() as f:
        pairs = [[normalize_string(s) for s in l.split("\t")] for l in f.split("\n")]

        if reversed:
            pairs = [list(reversed(p)) for p in pairs]
            input_lang = Lang(lang_2)
            output_lang = Lang(lang_1)
        else:
            input_lang = Lang(lang_1)
            output_lang = Lang(lang_2)
        
        return input_lang, output_lang, pairs


        
