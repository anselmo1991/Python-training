import os
import fnmatch

def find_util(start_path, file_pattern="*", file_type="f"):
    matches = []
    for root, dirnames, filenames in os.walk(start_path):
        if file_type == "d":
            for dirname in fnmatch.filter(dirnames, file_pattern):
                matches.append(os.path.join(root, dirname))
        else:
            for filename in fnmatch.filter(filenames, file_pattern):
                matches.append(os.path.join(root, filename))
    return matches


print(find_util('/users/', '*.py', 'f'))
