# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the LICENSE file in
# the root directory of this source tree. An additional grant of patent rights
# can be found in the PATENTS file in the same directory.
#

import re
import torch
import jieba
import argparse

#from fairseq import dictionary



def replace(matched):
    return " " + matched.group("m") + " "

def tokenize_line_en(line):
    line = re.sub(r"\t", "", line)
    line = re.sub(r"^\s+", "", line)
    line = re.sub(r"\s+$", "", line)
    line = re.sub(r"\s+", " ", line)
    line = re.sub(r"(?P<m>\W)", replace, line)
    line = re.sub(r" +", " ", line)
    #line = re.sub(r'"', ' " ', line)
    #line = re.sub(r".", " . ", line)
    #line = re.sub(r",", " , ", line)
    #line = re.sub(r"@", r" @ ", line)
    #return line.split()
    return line

def tokenize_line_zh_char(line):
    line = re.sub(r"\t", "", line)
    line = re.sub(r"^\s+", "", line)
    line = re.sub(r"\s+$", "", line)
    line = re.sub(r"\s+", " ", line)

    return [c for c in line]

def tokenize_line_zh(line):
    line = re.sub(r"\t", "", line)
    line = re.sub(r"^\s+", "", line)
    line = re.sub(r"\s+$", "", line)
    line = re.sub(r"\s+", " ", line)

    seg_list = jieba.cut(line, cut_all=False)

    return [c for c in seg_list]

parser = argparse.ArgumentParser()
parser.add_argument("-src", nargs=1, required=True)
parser.add_argument("-tgt", nargs=1, required=True)

args = parser.parse_args()

with open(args.src[0], 'r') as srcf:
    lines = srcf.readlines()
    lines = [tokenize_line_en(x) for x in lines]
    with open(args.tgt[0], 'w') as tgtf:
        tgtf.writelines("\n".join(lines))    