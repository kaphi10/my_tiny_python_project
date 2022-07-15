#!/usr/bin/env python3
#print Hello world
#print("Hello world")

#using Function


import argparse

def main():
    parser =argparse.ArgumentParser(description="say hello")
    parser.add_argument("-n", "--name", metavar="name",
                        default="world",help="tima")
    args =  parser.parse_args()
   # get_args()
    print("hello"+  " "+ args.name + "!")

if __name__ == '__main__':
    main()