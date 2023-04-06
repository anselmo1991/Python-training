def convert_size(size_bytes):
    KB = 1024
    MB = KB * 1024
    GB = MB * 1024

    if size_bytes >= GB:
        return "{:.2f} GB".format(size_bytes / GB)
    elif size_bytes >= MB:
        return "{:.2f} MB".format(size_bytes / MB)
    elif size_bytes >= KB:
        return "{:.2f} KB".format(size_bytes / KB)
    else:
        return "{:.2f} Byte".format(size_bytes)

print(convert_size(19))
print(convert_size(12345))
print(convert_size(1011947))
print(convert_size(572090))
print(convert_size(999999999999))
print(convert_size(9223372036854775807))