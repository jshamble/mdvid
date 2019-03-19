import os
import codecs
import re

input_name = 'in.md'
tmp_name = 'tmp.md'
output_name = 'out.md'

youtube_begin_string = "https://www.youtube.com/watch?v="

## simple python program to transform youtube URLS to preview for markdown files; 
##run the script, then press ctrl k + V in VS Code to preview youtube vids.
## End format of URL: [![Watch the video](https://img.youtube.com/vi/qjmOIsQFnms/sddefault.jpg)](https://youtu.be/qjmOIsQFnms)
##Note, need to run with CMD, and type $ chcp 65001 into terminal before starting the program to read it in UTF-8 if using windows

youtube_regex = ('(?:https?:\/\/)?(?:youtu\.be\/|(?:www\.|m\.)?youtube\.com\/(?:watch|v|embed)(?:\.php)?(?:\?.*v=|\/))([a-zA-Z0-9\-_]+)(&t=([0-9]*(h|s|m))*)?')

with codecs.open(input_name, 'r', encoding='utf-8') as fi, \
	codecs.open(tmp_name, 'w', encoding='utf-8') as fo:
	
	for line in fi:
		new_line = line # do_processing(line) # do your line processing here
		if "http://www.youtube.com" in line or "https://www.youtube.com" in line:
			youtube_url = re.search(youtube_regex, new_line)
			#if(youtube_url == None):
			#	print("URL FOR LINE")
			#	print("LINE:: " + new_line)
			#	print(youtube_url)
			if(youtube_url != None):
				youtube_url_timestamp = youtube_url.groups()[1];
				if (youtube_url_timestamp == None):
					youtube_url_timestamp = ""
				youtube_url = youtube_url.groups()[0]
				#print("BEFORE" + new_line)
				new_line = re.sub(youtube_regex, '[![Watch the video](https://img.youtube.com/vi/' + youtube_url + '/sddefault.jpg)](' + youtube_begin_string + youtube_url + youtube_url_timestamp + ')', new_line)
				#print("SUBBED" + new_line)
		fo.write(new_line)
		
#os.remove(input_name) # remove original
os.rename(tmp_name, output_name) # rename temp to output name