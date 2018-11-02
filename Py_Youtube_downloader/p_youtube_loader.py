#!/usr/bin/pypy3
# -*- coding: utf-8 -*-

import os
from urllib.request import urlopen
from urllib.parse import urlparse, parse_qs


tmp_filename= 'downloaded_video'
tmp_dir_tapmlate=os.path.normpath('./tmp_download')
tmp_dir=os.path.abspath(tmp_dir_tapmlate)
#print(tmp_dir)


def pull_urlinfo(video_url):

    video_id = parse_qs(urlparse(video_url).query)['v'][0]
    url_data = urlopen('http://www.youtube.com/get_video_info?&video_id=' + video_id).read()
    url_info = parse_qs(url_data.decode('utf-8'))
    return url_info


def show_items_content(url_info):

    stream_map = str(url_info['url_encoded_fmt_stream_map'][0])
    v_info = stream_map.split(",")

    i = 0
    quality_items_txtinfo = {}
    quality_urls = {}
    quality_item_short = {}

    # several option of video's quality in youtube-server:
    for video in v_info:
        i += 1
        item = parse_qs(video)
        item_quality = item['quality'][0]
        # print(item_quality)
        item_types = item['type'][0]
        item_type_array = item_types.split(';')
        # print(item_type_array[0])

        quality_url = item['url'][0]
        # print(quality_url)
        quality_items_txtinfo[i] = str(item_quality) + ' ' + str(item_types)
        quality_item_short[i] = str(i) + ' ' + str(item_quality) + ' ' + str(item_type_array[0])
        quality_urls[i] = quality_url

    items_content = (quality_items_txtinfo, quality_urls, quality_item_short)
    return items_content


def analise(video_url):

    url_info = pull_urlinfo(video_url)

    items_content = show_items_content(url_info)

    quality_items_txtinfo = items_content[0]
    quality_item_short = items_content[2]

    for keys in quality_items_txtinfo:
        print("quality_mode: ", keys, "quality: ", quality_items_txtinfo[keys])

    return quality_item_short


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
    while buffer:

        buffer = downloading_file.read(1024)
        my_localdownloaded_file.write(buffer)
        done += 1024
        dload=(done / size) * 100
        stringload="\t downloaded:... %.0f %%"%(dload)
        print(stringload)


    print("Saved in ", my_file_addr)



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


