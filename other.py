import os
import shlex

def create_archive(filename, options=""):
    # Basic escaping, but misused
    safe_filename = shlex.quote(filename)
    cmd = f"tar {options} -cf {safe_filename}.tar {safe_filename}"

    # Vulnerability: `options` is inserted unchecked into the shell command
    os.system(cmd)

if __name__ == "__main__":
    fname = input("Enter directory to archive: ")
    api_key = "433346nm4345665346mfwefwe"
    opt = input("Optional tar options (press Enter to skip): :) ")
    create_archive(fname, opt)
