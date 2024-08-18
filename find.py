#find.py  02Aug2024  crs
"""
find files - a limited replacement for linux find cmd for Windows
Most wanted features
    Search recursively in specified directory
    Specify directory name regex
    Specify file name regex
    Specify file extension
    Specify command to execute for each file
        default: print file name
    Specify pattern in file file contents
            list line(s)
            choose file if line found / not found
            
"""
import os
import sys
import re
import textwrap
import argparse

search_dir = os.curdir
#search_dir = '..'
file_name = None
file_ext_pat = None
file_ext_pat = 'bat|py'
#file_ext_pat = 'bat'
line_pat = None
line_not_pat = None
#line_pat = 'import'
show_full_path = False
show_file_name = True
show_dir = True
show_lines = True

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--sdir=', type=str, dest='search_dir', default=search_dir,
                        help=("search directory"
                              " (default:current directory)"))
parser.add_argument('-f', '--file=', type=str, dest='file_name', default=file_name,
                        help=("Select files, pattern"
                             " (default: no particular file)"))
parser.add_argument('-x', '--ext=', type=str, dest='file_ext_pat', default=file_ext_pat,
                        help=("Select file extension, pattern"
                             " (default: all extensions"))
parser.add_argument('-l', '--line', type=str, dest='line_pat', default=line_pat,
                        help=("line matching pattern"
                             " (default: No line matching)"))
parser.add_argument('-n', '--not_line', type=str, dest='line_not_pat', default=line_not_pat,
                        help=("lines not matching pattern"
                             " (default: No not (veto) line matching)"))
parser.add_argument('--show_lines', type=bool, dest='show_lines', default=show_lines)
parser.add_argument('--show_full', type=bool, dest='show_full_path', default=show_full_path)
parser.add_argument('--show_dir', type=bool, dest='show_dir', default=show_dir)
parser.add_argument('--show_file', type=bool, dest='show_file_name', default=show_file_name)

args = parser.parse_args()             # or die "Illegal options"

search_dir = args.search_dir 
file_name = args.file_name
file_ext_pat = args.file_ext_pat
show_lines = args.show_lines
line_pat = args.line_pat
line_not_pat = args.line_not_pat
show_full_path = args.show_full_path
show_file_name = args.show_file_name
show_dir = args.show_dir





for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file_name is not None:
            if not re.match(file_name, file):
                continue    # No match for file
        if file_ext_pat is not None:
            match_file_ext = re.match(r'^.*\.([^.]*)$', file)      # Allow name.
            if not match_file_ext:
                continue    # No file extension
            
            file_ext = match_file_ext.group(1)
            
            if not re.match("^" + file_ext_pat + "$", file_ext):
                continue    # No match for file extension
        
        file_path = os.path.abspath(os.path.join(root, file))
        base_str = ""
        if show_full_path:
            base_str = file_path
        elif show_dir:
            file_dir = os.path.basename(os.path.dirname(file_path))
            base_str = os.path.join(file_dir, file)
        if line_pat is None and line_not_pat is None:
            print(base_str)    
            continue        # Only list file
        
        with open(file_path) as fp:
            for line in fp.readlines():
                if (line_pat is not None and re.search(line_pat, line)
                        or line_not_pat is not None and not re.search(line_not_pat, line)):
                    print(f"{base_str}: {line}", end="")

