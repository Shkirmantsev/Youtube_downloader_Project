#!/usr/bin/pypy3
# -*- coding: utf-8 -*-

import subprocess
import os, sys
from multiprocessing import Lock



@staticmethod
def convertinmp3(addr,my_file_addr,thr,lock):
    thr += 1
    print("self.threads: ",thr)
    normaddr=os.path.normpath(addr)
    fulladdr=os.path.abspath(normaddr)
    cmdline="ffmpeg -i {0} -f mp3 -ab 320000 -vn {1}".format(fulladdr,my_file_addr)
    with lock:
        subprocess.call(cmdline, shell=True)
    print("audio from: ",fulladdr)
    print("***END OF FILE***")
    thr -= 1
    with lock:
        print("self.threads: ", thr)
    sys.exit()





if __name__=="__main__":

    lock=Lock()

    testaddr = 'test1.mp4'

    thr = 0
    normtestaddr = os.path.normpath(testaddr)
    fulltestaddr = os.path.abspath(normtestaddr)
    testfile_dirname = os.path.dirname(fulltestaddr)
    filetestname = "music.mp3"
    my_file_addr = testfile_dirname + os.sep + filetestname

    class Test():
        convertinmp3=convertinmp3

            #convertinmp3(fulltestaddr, my_file_addr,thr,lock)

    Test.convertinmp3(fulltestaddr, my_file_addr,thr,lock)