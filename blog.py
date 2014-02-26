#!/usr/bin/python

"""
This is a utilty to help blogging with gor on Github

"""

import argparse
import os
import re
import subprocess

posts_dir = "posts"
temp_dir = "temp"
cur_dir = os.getcwd()

class IsNotDirException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, name):
        Exception.__init__(self)
        self.name = name

def do_compile():
    """ compile command implementation
    """
    rename_temp_files()
    do_gor_compile()

def do_gor_compile():
    subprocess.call(["gor", "compile"])

def rename_temp_files():
    print "In the current directory: " + cur_dir
    print ""

    temp_files = [f for f in os.listdir(posts_dir) if re.match(r'.*\.md~$', f)]
    if len(temp_files) == 0:
        print "No file is renamed"
        print ""
        return
        
    print "Renaming file(s):"
    for f in temp_files:
        old = os.path.join(posts_dir, f)
        new = os.path.join(temp_dir, f)
        os.renames(old, new)
        print "    Renamed '" + old + "' to '" + new + "'"
    print ""

def main():
    parser = argparse.ArgumentParser(description='A utility to help blogging with gor on Github')
    parser.add_argument("command", 
                        help="compile: move emacs temp files ending "
                        "with ~ to temp directory in the root of blog site "
                        "and compile the site")
    args = parser.parse_args()
    if args.command.lower() == "compile":
        do_compile()




if __name__ == "__main__":
    main()
