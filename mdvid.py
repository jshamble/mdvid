import os
import codecs
import re

##make sure to install pip install lxml

from lxml import etree
import requests


input_name = 'in.md'
tmp_name = 'tmp.md'
output_name = 'out.md'

print_title = True
print_desc = False

youtube_begin_string = "http://www.youtube.com/watch?v="

## simple python program to transform youtube URLS to preview for markdown files; 
## run the script, then press ctrl k + V in VS Code to preview youtube vids.
## possible start format: http://www.youtube.com/watch?v=AVXejOoPECA End format of URL: [![Watch the video](https://img.youtube.com/vi/AVXejOoPECA/sddefault.jpg)](https://youtu.be/AVXejOoPECA)
## Note, need to run with CMD, and type $ chcp 65001 into terminal before starting the program to read it in UTF-8 if using windows

youtube_regex = ('(?:https?:\/\/)?(?:youtu\.be\/|(?:www\.|m\.)?youtube\.com\/(?:watch|v|embed)(?:\.php)?(?:\?.*v=|\/))([a-zA-Z0-9\-_]+)(&t=([0-9]*(h|s|m))*)?')

with codecs.open(input_name, 'r', encoding='utf-8') as fi, \
	codecs.open(tmp_name, 'w', encoding='utf-8') as fo:
	
	for line in fi:
		new_line = line # do_processing(line) # do your line processing here
		if "http://www.youtube.com" in line or "https://www.youtube.com" in line:
			youtube_url = re.search(youtube_regex, new_line)
			if(youtube_url != None):
				youtube_url_timestamp = youtube_url.groups()[1];
				if (youtube_url_timestamp == None):
					youtube_url_timestamp = ""
				youtube_url = youtube_url.groups()[0]
				new_line = re.sub(youtube_regex, '[![Watch the video](https://img.youtube.com/vi/' + youtube_url + '/sddefault.jpg)](' + youtube_begin_string + youtube_url + youtube_url_timestamp + ')', new_line)
				
				if(print_title or print_desc):
					youtube_html = requests.get(youtube_begin_string + youtube_url) 
					youtube = etree.HTML(youtube_html.text)
				
				if(print_title):
					video_title = youtube.xpath("//span[@id='eow-title']/@title")
					title_to_be_decoded = ''.join(video_title)
					fo.write( (b'# ' + (title_to_be_decoded.encode('utf-8')) + b"\n").decode() )
					# print( title_to_be_decoded.encode("utf-8") )
				fo.write(new_line)
				if(print_desc):
					video_desc = youtube.xpath("//p[@id='eow-description']/text()")
					desc_to_be_decoded = ''.join(video_desc)
					fo.write( (b'# ' + (desc_to_be_decoded.encode('utf-8')) + b"\n").decode() )
					# print(desc_to_be_decoded.encode("utf-8"))
		
os.remove(output_name) # remove output
os.rename(tmp_name, output_name) # rename temp to output name