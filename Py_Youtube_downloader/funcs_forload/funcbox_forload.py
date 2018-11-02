#!/usr/bin/pypy3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.parse import urlparse, parse_qs


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


if __name__ == '__main__':
    print("testing 'pull_urlinfo \n' ")
    video_url= "https://www.youtube.com/watch?v=vKvHBde0RmA"
    urlinfo=pull_urlinfo(video_url)
    print(urlinfo)
    print("------------ \n testing 'pull_urlinfo \n -------\n' ")
    items_content = show_items_content(urlinfo)

    def contentprint(self):
        for key in self:
            print("==>>", key, end="************\n")


    contentprint(items_content)

