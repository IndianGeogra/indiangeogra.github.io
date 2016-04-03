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


# Open the random_file
shutil.copyfile('scripts/example_archive.html', 'archive.html')
shutil.copyfile('scripts/example_random.html', 'random.html')

# Open the archive
example_archive = open('archive.html', 'r')
archive_data = example_archive.read()
new_archive_data = archive_data
example_archive.close()

example_random = open('random.html', 'r')
random_data = example_random.read()
new_random_data = random_data
example_random.close()

for i_noc in range(number_of_comics):
    print('Rewriting comic Nr. ' + str(i_noc + 1) + '...')
    # Verify that the directory and files exist
    #ensure_dir(str(info_data[i_noc].nr))
    if os.path.exists(str(info_data[i_noc].nr) + '/comic.png') and \
       os.path.exists(str(info_data[i_noc].nr) + '/comic_small.png') and \
       os.path.exists(str(info_data[i_noc].nr) + '/comic_lazy.png'):
        pass
    else:
        raise InputError('Some of the files "comic.png", "comic_small.png" or "comic_lazy.png" are not defined.')
        
    # Copy the example index file
    shutil.copyfile('scripts/example_index.html',str(info_data[i_noc].nr) + '/index.html')
        
    # Open the file, replace all that needs to be replaced
    example_file = open(str(info_data[i_noc].nr) + '/index.html', 'r')
    filedata = example_file.read()
    example_file.close()
    
    newdata = filedata
    newdata = newdata.replace('ig271828_name', info_data[i_noc].name)
    newdata = newdata.replace('ig271828_nr', str(info_data[i_noc].nr))
    newdata = newdata.replace('ig271828_prev_nr', str(info_data[i_noc].prev_nr))
    newdata = newdata.replace('ig271828_next_nr', str(info_data[i_noc].next_nr))
    newdata = newdata.replace('ig271828_data', info_data[i_noc].data)
    if info_data[i_noc].orientation == 'h':
        newdata = newdata.replace('width="ig271828_width"', 'width="620px"')
    else:
        newdata = newdata.replace('width="ig271828_width"', 'height="640px"')


    # First comic is different
    if i_noc == 0:
        old_line = '<li><a style="padding: 12px 8px 12px 8px;" rel="prev" href="../1/" accesskey="p">&lt; Tуда</a></li>'
        new_line = '<li "padding: 12px 8px 12px 8px;"> &lt; Tуда </li>'
        newdata = newdata.replace(old_line, new_line)

        old_line = '<li><a style="padding: 12px 8px 12px 8px;" href="http://indiangeogra.github.io/1">&lt;&lt;</a></li>'
        new_line = '<li "padding: 12px 8px 12px 8px;"> &lt; &lt; </li>'
        newdata = newdata.replace(old_line, new_line)

    # And the last, too
    if i_noc == number_of_comics - 1:
        old_line = '<li><a style="padding: 12px 8px 12px 8px;" rel="next" href="../' + str(number_of_comics) + '/" accesskey="n">Сюда &gt;</a></li>'
        new_line = '<li "padding: 12px 8px 12px 8px;"> Сюда &gt; </li>'
        newdata = newdata.replace(old_line, new_line)

        old_line = '<li><a style="padding: 12px 8px 12px 8px;" href="http://indiangeogra.github.io">&gt;&gt;</a></li>'
        new_line = '<li "padding: 12px 8px 12px 8px;"> &gt; &gt; </li>'
        newdata = newdata.replace(old_line, new_line)


    example_file = open(str(info_data[i_noc].nr) + '/index.html', 'w')
    example_file.write(newdata)
    example_file.close()


    # Archive and random
    old_line = '	  <!-- ig271828_archive -->'
    new_line = \
               '''
          <!-- Начало новой ссылки -->
	  <a style="display: inline; padding: 0px 0px 0px 0px;" 
	     href="''' + str(info_data[i_noc].nr) + '''/comic.png" data-lightbox="comic" data-title="''' + info_data[i_noc].name + '''"
	     rel="lightbox[comic]">
	    	    <img src="https://indiangeogra.github.io/''' + str(info_data[i_noc].nr) + '''/comic_lazy.png"
			 width="140px;"
			 title="''' + info_data[i_noc].name + '''" alt="''' + info_data[i_noc].name + '''" />
	  </a>
          <!-- Kонец новой ссылки -->

	  <!-- ig271828_archive -->'''
    new_archive_data = new_archive_data.replace(old_line, new_line)

    # random
    old_line = '<!-- ig271828_random -->'
    new_line = \
               ''',
                           "http://indiangeogra.github.io/''' + str(info_data[i_noc].nr) + '''"<!-- ig271828_random -->'''
    new_random_data = new_random_data.replace(old_line, new_line)

    shutil.copyfile(str(info_data[-1].nr) + '/index.html', 'index.html')

    
example_archive = open('archive.html', 'w')
example_archive.write(new_archive_data)
example_archive.close()

example_random = open('random.html', 'w')
example_random.write(new_random_data)
example_random.close()













