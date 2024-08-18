#list_file_extensions.py  30Jul2024  crs
"""
List files which have extensions
"""
import os
import sys
import re
import textwrap

#File types blocked by Gmail are:
ext_blocked_str = """
.ade, .adp, .apk, .appx, .appxbundle, .bat,
.cab, .chm, .cmd, .com, .cpl, .diagcab,
.diagcfg, .diagpkg, .dll, .dmg, .ex, .ex_,
.exe, .hta, .img, .ins, .iso, .isp, .jar,
.jnlp, .js, .jse, .lib, .lnk, .mde, .mjs,
.msc, .msi, .msix, .msixbundle, .msp, .mst,
.nsh, .pif, .ps1, .scr, .sct, .shb, .sys,
.vb, .vbe, .vbs, .vhd, .vxd, .wsc, .wsf,
.wsh, .xll,
"""
def check_file_ext(search_dir, ext_list=ext_blocked_str, verbose=False):
    """ Check for files with said extensions
    :ext_list: string with ,  separators
    :verbose: display operation default: False - no listing
    :returns: list of files with said extensions
    """
    if not os.path.exists(search_dir):
        print(f"Can't find {search_dir}")
        exit(1)

    if not os.path.isdir(search_dir):
        print(f"{search_dir} is not a directory")
        exit(2)
    
    if type(ext_list) == str:    
        raw_exts = re.findall(r'\.\w+', ext_list)
        exts = [rext[1:] for rext in raw_exts]
    else:
        exts = ext_list
    if verbose:
        print(textwrap.fill(f"exts: {" ".join(exts)}", width=60))

    files_exts = []     # list of file paths which have extensions
    
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            for ext in exts:
                if file.endswith("."+ext):
                    if verbose:
                        print(ext, os.path.join(root, file))
                    files_exts.append(os.path.join(root, file))
    return files_exts

if __name__ == '__main__':    
    search_dir = r"C:\Users\raysm\vscode\Introduction-To-Programming\src"
    search_dir = r"C:\Users\Owner\OneDrive\Desktop\intro_testing"
    if len(sys.argv) > 1:
        search_dir = sys.argv[1]
    else:
        inp = input(f"Enter search directory[{search_dir}]:")
        if inp != "":
            search_dir = inp

    check_file_ext(search_dir, verbose=True)