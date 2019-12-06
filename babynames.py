#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import argparse

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 - Extract the year and print it
 - Extract the names and rank numbers and just print them
 - Get the names data into a dict and print it
 - Build the [year, 'name rank', ... ] list and print it
 - Fix main() to use the extract_names list
"""
author = "__Bryan__"


def extract_names(filename):
    year = re.search(r'\d+', filename)
    names = []

    with open(filename, 'r') as f:
        f_contents = f.read()

        pattern = re.compile(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>')
        matches = pattern.finditer(f_contents)

        for match in matches:

            males = match.group(2) + " " + match.group(1)
            females = match.group(3) + " " + match.group(1)
            names.append(males)
            names.append(females)

        names.sort()
        names.insert(0, year.group())

    return names


def write_to_file(name_list, file_source):
    output_file = file_source + ".summary"

    with open(output_file, 'w') as wf:
        for text in name_list:
            wf.write(text + '\n')


def create_parser():
    """Create a cmd line parser object with 2 argument definitions"""
    parser = argparse.ArgumentParser(description="Extracts and alphabetizes baby names from html.")
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more filenames.
    # It will also expand wildcards just like the shell, e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+') # will make into a list
    return parser


def main(args):

    parser = create_parser()
    ns = parser.parse_args(args)        

    if not ns:
        parser.print_usage()
        sys.exit(1)

    for file in ns.files:
        names = extract_names(file)

        if not ns.summaryfile:    # if we dont have summary file flag, print
            print(names)
        else:
            write_to_file(names, file)


if __name__ == '__main__':
    main(sys.argv[1:])
