# mdvid

## A python (3) script that parses markdown files, finds youtube urls, and replaces them with video previews with thumbnails.

## Supports mulitlanguage titles (utf-8)

### usage: converting more vidoes into a previewable format: 

python mdvid.py (make sure to use python 3, you may need to create an alias for it)

inputfile = in.md
outputfile = out.md

### viewing

Preview any output md file with Visual studio code with the following key sequence: open the file (file.md), then
"( cmd(mac) or ctrl(windows) ) + k" then press "v". the preview with youtube video thumbnails should now be located in the newly opened tab to your right. Happy Listening!

#### Regex tested with to https://regexr.com/ and stackoverflow... includes timestamps, playlists and others... any feedback / non-working input is welcome, will update the regex as nesc. Wish to also preview html pages with a similar method; alas, perhaps this is not possible...

## Copyright Jonathan Shamblen 2019 MIT License
