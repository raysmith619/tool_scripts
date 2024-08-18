#make_intro_copy.py   12Aug2024  crs
""" 
Make emailable folder of distribution
"""
import os
import sys
import re
import shutil
import time
from list_file_extensions import check_file_ext
    
dev_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
src_base_dir = os.path.join(dev_dir, "Introduction-To-Programming")
dst_base_dir = r"C:\Users\Owner\OneDrive\Desktop"
dst_dir = "intro_testing"


src_file_dirs = ["Cheat_Sheet",            
            "exercises",
            "log",
            "my_work",
            "presentation",
            r"Docs\ForTheBlind\LessonPlans\8thGradeBlind",
            r"..\resource_lib",
            r"Docs\what_is_programming.docx",
            r"..\resource_lib\src\run_setup_turtle_braille.py",
            r"..\resource_lib\src\wx_square_loop_colors.py",
            ]
###src_file_dirs = ["Cheat_Sheet", "my_work",r"..\resource_lib\src\run_setup_turtle_braille.py",]   # Short list for test/debug

def is_dir(path):
    """ Check if it is our directory (or our file)
    :path: path name
    :returns: True if path is a directory
    """
    if re.match(r'^.*\.[^.]{2,4}$', path):
        return False
    
    return True

def check_file_dir(name, is_dir=True):
    """Check if exists and a directory
    :name: full path name
    :is_dir: is a directory default:True
    """
    if not os.path.exists(name):
        print(f"{name} not found")
        exit(1)
    if is_dir:
        if not os.path.isdir(name):
            print(f"{name} is not a directory")
            exit(1)
    else:
        if os.path.isdir(name):
            print(f"{name} is a directory")
            exit(1)

# Don't copy obvious Google email rejections
ignore_fun = shutil.ignore_patterns('*.bat', '*.exe.', '.venv')
def copy_file_dir(src, dst):
    """ Copy file or directory from src to dst
    :src: source file/directory 
    :dst: destination file/directory
    """
    dir_copy = os.path.isdir(src)
    dcstr = "dir " if dir_copy else "file"
    ddstr = " "*len(dcstr)
    print(f"copying {dcstr} {os.path.abspath(src)}\n"
          f"        {ddstr} to {dst}")
    if dir_copy:
        shutil.copytree(src, dst, ignore=ignore_fun)
    else:
        shutil.copyfile(src, dst)

check_file_dir(src_base_dir)
for src_file_dir in src_file_dirs:
    is_a_dir = is_dir(src_file_dir)
    check_file_dir(os.path.join(src_base_dir, src_file_dir), is_dir=is_a_dir)
    
if len(sys.argv) > 1:
    dst_dir = sys.argv[1]
    dst_full_dir = os.path.join(dst_base_dir, dst_dir)
else:
    dst_full_dir = os.path.join(dst_base_dir, dst_dir)

while True:
    inp = input(f"Enter full dst dir[{dst_full_dir}]:")
    if inp == "":
        dst_full_dir_candidate = dst_full_dir
    else:
        dst_full_dir_candidate = inp
            
    dst_base_dir = os.path.dirname(dst_full_dir_candidate)
    if not os.path.exists(dst_base_dir):
        print(f"Destination base {dst_base_dir} does not exist")
        continue
    
    if os.path.exists(dst_full_dir_candidate):
        print(f"Destination directory {dst_full_dir_candidate} already exists")
        continue
    
    break
    
dst_full_dir = dst_full_dir_candidate
dst_base_dir = os.path.dirname(dst_full_dir)

ans = "y"
inp = input(f"Create destination: {dst_full_dir} [{ans}]:")
if inp != "":
    ans = inp.lower()
if ans != "y":
    exit(0)

print(f"Creating {dst_full_dir}")
copy_start = time.time()    
for src_file_dir in src_file_dirs:
    src = os.path.join(src_base_dir, src_file_dir)
    dst = os.path.join(dst_full_dir, os.path.basename(src))
    copy_file_dir(src, dst)
copy_end = time.time()
copy_dur = copy_end - copy_start
print(f"Copy duration: copy_dur: {copy_dur:.2f} seconds")    
print(f"Checking for Google email dissalowed files")
file_exts = check_file_ext(dst_full_dir)
if len(file_exts) > 0:
      print(f"Files with Google blocked exs:\n\t{"\n\t".join(file_exts)}")
else:
    print("No blocked files found")