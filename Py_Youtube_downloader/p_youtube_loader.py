#!/usr/bin/pypy3
# -*- coding: utf-8 -*-

import os


#####
from funcs_forload.funcbox_forload import show_items_content
from funcs_forload.funcbox_forload import pull_urlinfo
from funcs_forload.downldfunc import downloadurl_file
#####

tmp_filename= 'downloaded_video'
tmp_dir_tapmlate=os.path.normpath('./tmp_download')
tmp_dir=os.path.abspath(tmp_dir_tapmlate)
#print(tmp_dir)


def analise(video_url):

    url_info = pull_urlinfo(video_url)

    items_content = show_items_content(url_info)

    quality_items_txtinfo = items_content[0]
    quality_item_short = items_content[2]

    for keys in quality_items_txtinfo:
        print("quality_mode: ", keys, "quality: ", quality_items_txtinfo[keys])

    return quality_item_short



def get_videofile(video_url, directory=None, file_name=None, quality_mode=1):

    url_info = pull_urlinfo(video_url)

    title = url_info['title'][0]
    # print(title)
    directory=directory or tmp_dir
    directory = os.path.normpath(directory)

    if not os.path.exists(directory):
        os.mkdir(directory)

    print(directory)



    if file_name == None:
        my_filename = str(title).replace("/", "-") + '.mp4'
    else:
        my_filename = str(file_name).replace("/", "-")

    print(my_filename)


    items_content = show_items_content(url_info)
    quality_items_txtinfo = items_content[0]
    quality_urls = items_content[1]


    for keys in quality_items_txtinfo:
        print("quality_mode: ", keys, "quality: ", quality_items_txtinfo[keys])

    addr_for_download = quality_urls[quality_mode]

    downloadurl_file(addr_for_download, directory, my_filename)





if __name__ == '__main__':

    test=input('enter url: \n')
    test=test or 'https://www.youtube.com/watch?v=vKvHBde0RmA'
    test=str(test)

    get_videofile(test)


