#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import shutil
import string

reload(sys)  
sys.setdefaultencoding('utf8')

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)


execfile('scripts/comic_info.py')

# Verify that the directory and files exist
ensure_dir('../' + str(info_data[-1].nr))
if os.path.exists(str(info_data[-1].nr) + '/comic.png') and \
   os.path.exists(str(info_data[-1].nr) + '/comic_small.png') and \
   os.path.exists(str(info_data[-1].nr) + '/comic_lazy.png'):
    pass
else:
    raise InputError('Some of the files "comic.png", "comic_small.png" or "comic_lazy.png" are not defined.')

# Copy the example index file
shutil.copy('scripts/example_index.html',str(info_data[-1].nr) + '/index.html')

# Open the file, replace all that needs to be replaced
example_file = open(str(info_data[-1].nr) + '/index.html', 'r')
filedata = example_file.read()
example_file.close()

newdata = filedata
newdata = newdata.replace('ig271828_name', info_data[-1].name)
newdata = newdata.replace('ig271828_nr', str(info_data[-1].nr))
newdata = newdata.replace('ig271828_prev_nr', str(info_data[-1].prev_nr))
newdata = newdata.replace('ig271828_next_nr', str(info_data[-1].next_nr))
newdata = newdata.replace('ig271828_data', info_data[-1].data)
if info_data[-1].orientation == 'h':
    newdata = newdata.replace('width="ig271828_width"', 'width="620px"')
else:
    newdata = newdata.replace('width="ig271828_width"', 'height="640px"')


example_file = open(str(info_data[-1].nr) + '/index.html', 'w')
example_file.write(newdata)
example_file.close()



# Open the archive, add necessary lines
example_archive = open('archive.html', 'r')
filedata = example_archive.read()
example_archive.close()

newdata = filedata
old_line = '	  <!-- ig871828_archive -->'
new_line = \
'''
          <!-- Начало новой ссылки -->
	  <a style="display: inline; padding: 0px 0px 0px 0px;" 
	     href="''' + str(info_data[-1].nr) + '''/comic.png" data-lightbox="comic" data-title="''' + info_data[-1].name + '''"
	     rel="lightbox[comic]">
	    	    <img src="https://indiangeogra.github.io/''' + str(info_data[-1].nr) + '''/comic_lazy.png"
			 width="140px;"
			 title="''' + info_data[-1].name + '''" alt="''' + info_data[-1].name + '''" />
	  </a>
          <!-- Kонец новой ссылки -->

	  <!-- ig871828_archive -->'''
newdata = newdata.replace(old_line, new_line)

example_file = open('archive.html', 'w')
example_file.write(newdata)
example_file.close()



# Open the random_file, add necessary lines
example_random = open('random.html', 'r')
filedata = example_random.read()
example_random.close()

newdata = filedata
old_line = '<!-- ig271828_random -->'
new_line = \
''',
                           "http://indiangeogra.github.io/''' + str(info_data[-1].nr) + '''"<!-- ig271828_random -->'''
newdata = newdata.replace(old_line, new_line)

example_file = open('random.html', 'w')
example_file.write(newdata)
example_file.close()

shutil.copyfile(str(info_data[-1].nr) + '/index.html', 'index.html')


