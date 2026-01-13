import struct
import zlib


def read_dword(cache_file):
    data = cache_file.read(4)
    return struct.unpack('<I', data)[0]


def read_qword(cache_file):
    dwords = struct.unpack('<II', cache_file.read(8))
    buffer = struct.pack('<II', dwords[1], dwords[0])
    return struct.unpack('<Q', buffer)[0]


def read_resource_data(cache_file, start, length):
    current_position = cache_file.tell()

    cache_file.seek(start)
    data = cache_file.read(length)

    cache_file.seek(current_position)
    return data


def load_cache_file(filename):
    print(filename)
    cache_file = open(filename, 'rb')
    # get the indeces count for the file
    num_resources = read_dword(cache_file)
    read_dword(cache_file)
    read_dword(cache_file)
    read_dword(cache_file)

    resources = []
    # cache indeces
    for _ in range(num_resources):
        resource_id = read_qword(cache_file)
        resource_offset = read_dword(cache_file)
        resource_decompressed_len = read_dword(cache_file)
        resource_compressed_len = read_dword(cache_file)

        resource_data = read_resource_data(
            cache_file,
            resource_offset,
            resource_compressed_len
        )

        if resource_decompressed_len > resource_compressed_len:
            resource_data = zlib.decompress(resource_data)

        resources.append([
            resource_id,
            resource_data
        ])

    return resources


def write_dword(cache_file, value):
    data = struct.pack('<I', value)
    cache_file.write(data)


def write_qword(cache_file, value):
    qword = struct.pack('<Q', value)
    dwords = [
        struct.unpack('<I', qword[:4])[0],
        struct.unpack('<I', qword[4:])[0],
    ]
    data = struct.pack('<II', dwords[1], dwords[0])
    cache_file.write(data)


def write_bytes(cache_file, value):
    cache_file.write(value)


def save_cache_file(filename, resources, compress=True):
    cache_file = open(filename, 'wb')

    num_resources = len(resources)

    last_offset = 0
    last_offset += 0x10  # header
    last_offset += num_resources * 0x14  # resource_headers

    data_start = last_offset
    for resource in resources:
        resource.append(last_offset)
        resource.append(len(resource[1]))

        if compress:
            resource[1] = zlib.compress(resource[1])
        resource.append(len(resource[1]))

        last_offset += resource[4]

    data_end = last_offset
    write_dword(cache_file, num_resources)
    write_dword(cache_file, data_start)
    write_dword(cache_file, data_end)
    write_dword(cache_file, 0xffffffff)
    for resource in resources:
        write_qword(cache_file, resource[0])
        write_dword(cache_file, resource[2])
        write_dword(cache_file, resource[3])
        write_dword(cache_file, resource[4])

    for resource in resources:
        write_bytes(cache_file, resource[1])
