#!/usr/bin/pypy3
#  -*- coding: utf-8 -*-

"""
version 1.0
#################################################################################
launch GUI interface for P_youtube_loader.py
#################################################################################
"""

import funcs_forload.supportfuncsbox
from multiprocessing import Value, Lock

from funcs_forload.main_py import main_array

from tkinter import *

import p_youtube_loader, os, sys, _thread                # FTP getfile here, not socket

from form import Form




class FtpForm(Form):
    def __init__(self):
        self.lock=Lock()
        text = ''
        self.root = Tk()
        root=self.root

        #root.title('Youtube Downloader by Shkirmantsev')
        root.title(self.title)
        labels = ['video_url for download:',
                  'quality_mode or press enter',
                  'Saving_directory',
                  'Saving_file_name',
                  'video_file_to_convert']

        Form.__init__(self, labels, parent=root)

        self.mutex = _thread.allocate_lock()

        threadsv=Value('i',0)
        self.threads = threadsv.value

        #print("self content on start: ",self.content)
        self.content['quality_mode or press enter'].delete(0, END)
        self.content['quality_mode or press enter'].insert(0, 1)
        #print("content is: ", self.content)

        # import functions
        for items in main_array:
            exec("from {0} import {1} as {1}".format(items[1],items[0]))
            #assert "." not in items[0], "Houston we've got a problem with hakers"
            if ("import" in items[0]) or ("." in items[0]): raise Exception("Houston we've got a problem with hakers")
            func=eval("{0}".format(items[0]))
            setattr(FtpForm,"{0}".format(items[0]),func)

        root.mainloop()


        #print(directory,file_name,sep="\n")



class FtpGetfileForm(FtpForm):
    title = 'Youtube Downloader by Shkirmantsev'

    def do_transfer(self, video_url, directory,file_name, quality_mode):
        lock=self.lock
        try:
            p_youtube_loader.get_videofile(video_url, directory,file_name, quality_mode)
        finally:
            self.threads -= 1
            # self.mutex.acquire()


            #self.mutex.release()
            print("Finished!!!!")



if __name__ == '__main__':
    FtpGetfileForm()

