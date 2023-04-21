import os
import win32security
from prettytable import PrettyTable

def get_file_owner(file_path:str):
    sd = win32security.GetFileSecurity(file_path, win32security.OWNER_SECURITY_INFORMATION)
    owner_sid = sd.GetSecurityDescriptorOwner()
    name, domain, type = win32security.LookupAccountSid(None, owner_sid)
    return name

def get_file_group(file_path:str):
    sd = win32security.GetFileSecurity(file_path, win32security.GROUP_SECURITY_INFORMATION)
    owner_sid = sd.GetSecurityDescriptorGroup()
    name, domain, type = win32security.LookupAccountSid(None, owner_sid)
    return name

def get_file_info(file_path):
    file_stat = os.stat(file_path)
    file_mode = oct(file_stat.st_mode)[-3:]
    file_owner_name = get_file_owner(file_path)
    file_group_name = get_file_group(file_path)
    file_size = file_stat.st_size
    file_name = os.path.basename(file_path)

    return file_mode, file_owner_name, file_group_name, file_size, file_name


def list_directory(path):
    files = os.listdir(path)
    table = PrettyTable(['Mode', 'Owner', 'Group', 'Size', 'File name'])

    for file_name in files:
        file_path = os.path.join(path, file_name)
        file_info = get_file_info(file_path)
        table.add_row([file_info[0], file_info[1], file_info[2], file_info[3], file_info[4]])

    print(table)


list_directory("/users/Sofia_Shilova/Python-training")
