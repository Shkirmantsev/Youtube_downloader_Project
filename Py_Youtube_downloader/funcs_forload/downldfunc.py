
#!/usr/bin/pypy3
# -*- coding: utf-8 -*-

import os
from urllib.request import urlopen


def downloadurl_file(addr_for_download, directory, my_filename):

    print("you select", addr_for_download)

    downloading_file = urlopen(addr_for_download)
    # print(downloading_file.headers)

    size = int(downloading_file.headers['Content-Length'])
    # print(size)

    done = 0

    my_file_addr = directory + os.sep + my_filename
    # print(my_file_addr)

    my_localdownloaded_file = open(my_file_addr, "wb+")

    buffer = True
    try:
        buffer = downloading_file.read(1024)
        while buffer:

            my_localdownloaded_file.write(buffer)
            done += 1024
            dload = (done / size) * 100
            stringload = "\t downloaded:... %.0f %%" % (dload)
            print(stringload)
            buffer = downloading_file.read(1024)
    except:
        print("can not write or read from internet downloading file")
    finally:
        my_localdownloaded_file.close()

    downloading_file.close()

    print("Saved in ", my_file_addr)