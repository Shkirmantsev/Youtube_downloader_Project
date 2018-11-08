#!/usr/bin/pypy3
#  -*- coding: utf-8 -*-

"""
version 0.1
#################################################################################
launch GUI interface for P_youtube_loader.py
#################################################################################
"""

from tkinter import *
from tkinter.messagebox import showinfo
import p_youtube_loader, os, sys, _thread                # FTP getfile here, not socket
import pyperclip
from form import Form     # reuse form tool in socket dir
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import showerror

class FtpForm(Form):
    def __init__(self):
        text = ''
        root = Tk()

        #root.title('Youtube Downloader by Shkirmantsev')
        root.title(self.title)
        labels = ['video_url for download:',
                  'quality_mode or press enter',
                  'Saving_directory',
                  'Saving_file_name']

        Form.__init__(self, labels, entrsize=80, parent=root)
        self.mutex = _thread.allocate_lock()
        self.threads = 0
        self.content['quality_mode or press enter'].delete(0, END)
        self.content['quality_mode or press enter'].insert(0, 1)
        print("content is: ", self.content)


    def transfer(self, video_url, directory=None, file_name=None, quality_mode=None, ):
        try:
            self.do_transfer(video_url, directory,file_name, quality_mode)
            #print('saved in "%s"'  % (p_youtube_loader.tmp_dir))
        except:
            print('Download failed', end=' ')
            print(sys.exc_info()[0], sys.exc_info()[1])
        self.mutex.acquire()
        self.threads -= 1
        self.mutex.release()

    def onSubmit(self):
        #Form.onSubmit(self)
        video_url = self.content['video_url for download:'].get()
        print(video_url)
        quality_mode  = int(self.content['quality_mode or press enter'].get())
        print(quality_mode)

        directory = self.content['Saving_directory'].get()
        if directory == '': directory = None
        else: directory = os.path.normpath(directory)


        file_name = self.content['Saving_file_name'].get()
        if file_name == '': file_name = None
        else: file_name = os.path.normpath(directory)
        print(file_name)




        self.mutex.acquire()
        self.threads += 1
        self.mutex.release()
        ftpargs = (video_url, directory,  file_name, quality_mode)
        _thread.start_new_thread(self.transfer, ftpargs)
        showinfo(self.title, 'download of "%s" started' % (p_youtube_loader.tmp_filename))

    def onCancel(self):
        if self.threads == 0:
            Tk().quit()
        else:
            showinfo(self.title,
                     'Cannot exit: %d threads running' % self.threads)
    def onSave(self):                                      # save as file dialog
        save_as_file=asksaveasfilename()
        directory=os.path.dirname(save_as_file)

        file_name=os.path.basename(save_as_file)
        self.content['Saving_directory'].delete(0,END)
        self.content['Saving_directory'].insert(0,str(directory))
        self.content['Saving_file_name'].delete(0,END)
        self.content['Saving_file_name'].insert(0,str(file_name))


        #print(directory,file_name,sep="\n")

    def onPaste(self):
        try:
            self.text=pyperclip.paste()
            pp=self.text
            print(pp)
        except TclError:
            showerror('Youtube Downloader','Nothing to paste into URL-field from Clipboard')
            return
        self.content['video_url for download:'].insert(0,str(self.text))

    def add_quality(self):
        video_url = self.content['video_url for download:'].get()
        self.content_modes=p_youtube_loader.analise(video_url)
        content_modes=self.content_modes
        print(content_modes)
        self.update_button()

    def onPress(self):
        pick=self.var.get()
        #print('you pressed ', pick)
        #print('result',self.content_modes[pick])
        self.content['quality_mode or press enter'].delete(0, END)
        self.content['quality_mode or press enter'].insert(0, pick)







class FtpGetfileForm(FtpForm):
    title = 'Youtube Downloader by Shkirmantsev'

    def do_transfer(self, video_url, directory,file_name, quality_mode):
        p_youtube_loader.get_videofile(video_url, directory,file_name, quality_mode)


if __name__ == '__main__':
    FtpGetfileForm()
    mainloop()
