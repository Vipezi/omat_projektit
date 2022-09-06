#! /usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description = "tell here what your program will do")
parser.add_argument('-f', '--first', help="tell here what is the first argument, how to use it", required = True)
parser.add_argument('-s', '--second', help="tell here what is the second argument, how to use it", required = True)

args = vars(parser.parse_args())
print(args)
print(args["first"])