Playlist.py
===========

Playlist.py is a quick and dirty way to create a living textfile queued youtube video downloader. This tool is meant to be used in cohesion with a [cron job](http://www.generateit.net/cron-job/) of your preference

***Important Notes:*** Ensure that your system has [youtube-dl](http://rg3.github.com/youtube-dl/) installed on it before running this script.

Usage
-----

1.) Create a ***Playlist.txt*** file in a directory of your choosing, and fill it up with youtube urls. 

Playlist.txt 
http://www.youtube.com/watch?v=co5gy_2uOEY
http://www.youtube.com/watch?v=bvRXQTyBezk

2.) Run It!

	$$python Playlist.py -p [path of Playlist.txt file]

### Sample Playlist.txt 
	http://www.youtube.com/watch?v=gSW5Fr48jVU
	http://www.youtube.com/watch?v=ltun92DfnPY
	


