#!/usr/bin/env python3

import argparse
from pysgf import SGF

parser = argparse.ArgumentParser()
parser.add_argument("--sgf", '-f', help="SGF file to convert")
args = parser.parse_args()

root = SGF.parse_file(args.sgf)
flattened_sgf = []

def get_child(sgf_obj: SGF) -> SGF:

  if hasattr(sgf_obj, "children"):
    return sgf_obj.children


def get_all_children(sgf_obj: SGF) -> list:

  children = get_child(sgf_obj)

  if children:
    for child in children:
      move = str(child.move).replace("Move(W", "")
      move = move.replace("Move(B", "")
      move = move.replace(")", "")
      flattened_sgf.append(move)
      get_all_children(child)

get_all_children(root)
print(flattened_sgf)
