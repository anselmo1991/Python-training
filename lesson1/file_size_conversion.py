def file_size(size_bytes):
    kb = 1024
    mb = kb * 1024
    gb = mb * 1024

    if size_bytes >= gb:
        return "{:.2f} gb".format(size_bytes / gb)
    elif size_bytes >= mb:
        return "{:.2f} mb".format(size_bytes / mb)
    elif size_bytes >= kb:
        return "{:.2f} kb".format(size_bytes / kb)
    else:
        return "{:.2f} Byte".format(size_bytes)

print(file_size(19))
print(file_size(12345))
print(file_size(1011947))
print(file_size(572090))
print(file_size(999999999999))
print(file_size(9223372036854775807))
