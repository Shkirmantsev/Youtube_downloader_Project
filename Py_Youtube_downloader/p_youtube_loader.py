#!/usr/bin/pypy3
# -*- coding: utf-8 -*-

import os
from urllib.request import urlopen
from urllib.parse import urlparse, parse_qs

tmp='downloaded_video'
tmp_dir='./tmp_download/'
#print(tmp_dir)
tmp_dir=os.path.abspath(tmp_dir)
#print(tmp_dir)

def analise(video_url, quality_mode=5):
    video_id = parse_qs(urlparse(video_url).query)['v'][0]
    url_data = urlopen('http://www.youtube.com/get_video_info?&video_id=' + video_id).read()
    url_info = parse_qs(url_data.decode('utf-8'))

    stream_map = str(url_info['url_encoded_fmt_stream_map'][0])
    v_info = stream_map.split(",")
    i = 0
    quality_item = {}
    quality_urls = {}
    quality_item_short = {}
    for video in v_info:
        i += 1
        item = parse_qs(video)
        a = item['quality'][0]
        #print(a)
        b = item['type'][0]
        ttt=b.split(';')
        #print(ttt[0])

        quality_url = item['url'][0]
        # print(quality_url)
        quality_item[i] = str(a) + ' ' + str(b)
        quality_item_short [i]= str(i)+' '+str(a)+' '+str(ttt[0])
        quality_urls[i] = quality_url


    for keys in quality_item:
        print("quality_mode: ", keys, "quality: ", quality_item[keys])
    return quality_item_short




def get_videofile(video_url, directory=tmp_dir, file_name=tmp, quality_mode=5):
    video_id = parse_qs(urlparse(video_url).query)['v'][0]
    url_data = urlopen('http://www.youtube.com/get_video_info?&video_id=' + video_id).read()
    url_info = parse_qs(url_data.decode('utf-8'))
    title = url_info['title'][0]
    # print(title)
    directory = os.path.normpath(directory)
    tmp_dir = directory
    print(directory)
    if file_name == 'downloaded_video':
        my_fileName = str(title).replace("/", "-") + '.mp4'
    else:
        my_fileName = str(file_name).replace("/", "-")
    print(my_fileName)
    # token_value = url_info['token']
    # download_url = "http://www.youtube.com/get_video?video_id={0}&t={1}&fmt=18".format(
    # video_id, token_value)
    stream_map = str(url_info['url_encoded_fmt_stream_map'][0])
    # print(stream_map)
    v_info = stream_map.split(",")
    # print(v_info)

    i = 0
    quality_item = {}

    quality_urls = {}
    for video in v_info:
        i += 1
        item = parse_qs(video)
        a = item['quality'][0]
        # print(a)
        b = item['type'][0]
        # print(b)
        quality_url = item['url'][0]
        # print(quality_url)
        quality_item[i] = str(a) + ' ' + str(b)
        quality_urls[i] = quality_url

    for keys in quality_item:
        print("quality_mode: ", keys, "quality: ", quality_item[keys])

    print("you select", quality_urls[quality_mode])

    downloading_file = urlopen(quality_urls[quality_mode])
    # print(downloading_file.headers)

    size = int(downloading_file.headers['Content-Length'])
    # print(size)
    buffer = downloading_file.read(1024)
    done = 0
    my_file_addr = directory + os.sep + my_fileName
    # print(my_file_addr)
    addr = my_file_addr

    my_file_addr = open(my_file_addr, "wb+")


    while buffer:
        my_file_addr.write(buffer)
        done += 1024
        dload=(done / size) * 100
        stringload="\t downloaded:... %.1f %%"%(dload)
        print(stringload)
        buffer = downloading_file.read(1024)

    print("Saved in ", addr)




if __name__ == '__main__':
    test=input('enter url: \n')
    test=str(test)
    #test='https://www.youtube.com/watch?v=vKvHBde0RmA'
    get_videofile(test)


