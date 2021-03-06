import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Creates index.html file.')
parser.add_argument('--number', '-n', type=int)
parser.add_argument('--name', type=str)
parser.add_argument('--onclick', type=str)
parser.add_argument('--width', '-w', default=620, type=int)
args = parser.parse_args()

n_prev = max(args.number - 1, 1) # Number of the previous comic, not less than 1
n_next = args.number + 1
home_link = 'http://indiangeogra.github.io/'
home_link_s = 'https://indiangeogra.github.io/'

s1 = \
"""<!DOCTYPE html>
<html>
  <head>
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
    <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Forum">
    <link rel="stylesheet" type="text/js" href="https://fonts.googleapis.com/css?family=Forum">

    <script src="https://indiangeogra.github.io/javascripts/lazysizes.min.js" async=""></script>
    <script type="text/javascript" src='http://indiangeogra.github.io/javascripts/shortcuts.js'></script>
"""

s2 = \
"""
    <script type="text/javascript">
      shortcut.add("Left",function() {
      window.location.href = 'http://indiangeogra.github.io/""" + str(n_prev) + \
"""';
      });
      shortcut.add("Right",function() {
      window.location.href = '""" + str(n_next) + \
"""';
      });
    </script>
"""

s3 = \
"""
    <style>
      body {
        font-family: 'Forum', serif;
        font-size: 48px;
      }
    </style>
    
    <style type="text/css">
      #share-buttons img {
      width: 35px;
      padding: 5px;
      border: 0;
      box-shadow: 0;
      display: inline;
    }
    </style>

    <!--<link href='https://fonts.googleapis.com/css?family=Tangerine' rel='stylesheet' type='text/css'>-->
    <link rel="stylesheet" type="text/css" href="https://indiangeogra.github.io/stylesheets/stylesheet.css" media="screen">
    <link rel="stylesheet" type="text/css" href="https://indiangeogra.github.io/stylesheets/pygment_trac.css" media="screen">
    <link rel="stylesheet" type="text/css" href="https://indiangeogra.github.io/stylesheets/print.css" media="print">
    <link rel="icon" href="https://indiangeogra.github.io/favicon.png">
    <link  rel="stylesheet" href="https://indiangeogra.github.io/stylesheets/lightbox.css">
    <!--[if lt IE 9]>
    <script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
    <meta name="msapplication-TileImage" content="favicon.png">
    <title>indian geogra: Размытый город</title>
    
    <script>
	(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  	(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  	m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  	})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
  	ga('create', 'UA-73773751-1', 'auto');
  	ga('send', 'pageview');
    </script>
  </head>
"""

s4 = \
"""
  <body>
    <div id="container">
      <div class="inner">


        <header>
          <h1><span 
		class="pseudolink" 	
   		onclick="location='http://indiangeogra.github.io'"
   		onmouseover="" style="cursor: pointer;">
          	indian geogra
          	</span>
          </h1>
          <h2>С неба про погоду</h2>
        </header>


        <section id="main_content">


          <div id="ComicTitle">""" + args.name + \
"""	  </div>


	  <div id="nav" style="padding: 12px 8px 12px 8px;">
	    <li><a style="padding: 12px 8px 12px 8px;" href="http://indiangeogra.github.io/1">&lt;&lt;</a></li>
	    <li><a style="padding: 12px 8px 12px 8px;" rel="prev" href="../""" + n_prev + \
"""/" accesskey="p">&lt; Tуда</a></li>
	    <li><a style="padding: 12px 8px 12px 8px;" href="http://indiangeogra.github.io/random.html">Куда-нибудь</a></li>
	    <li><a style="padding: 12px 8px 12px 8px;" rel="next" href="../""" + n_next + \
"""/" accesskey="n">Сюда &gt;</a></li>
	    <li><a style="padding: 12px 8px 12px 8px;" href="http://indiangeogra.github.io">&gt;&gt;</a></li>
	  </div>
	  <div id="comic">
	  <center>
	    <a style="display: inline; color: #303030; padding: 0px 0px 0px 0px;"
	       href="https://indiangeogra.github.io/""" + args.n + \
"""/comic.png">
	    <img src="https://indiangeogra.github.io/""" + args.n + \
'''/comic_lazy.png"
		 width="''' + args.w + '''px"
		 data-src="https://indiangeogra.github.io/''' + args.n +\
'''/comic_small.png"
		 class="lazyload blur-up"
		 title="1115" alt="''' + args.name + '''" class="lazyload no-src" />
	    </a>
	  </center>
	  </div>
''' + \
'''	  <div id="nav" style="padding: 12px 8px 12px 8px;">
	    <li><a style="padding: 12px 8px 12px 8px;" href="http://indiangeogra.github.io/1">&lt;&lt;</a></li>
	    <li><a style="padding: 12px 8px 12px 8px;" rel="prev" href="../''' + n_prev + \
'''/" accesskey="p">&lt; Tуда</a></li>
	    <li><a style="padding: 12px 8px 12px 8px;" href="http://indiangeogra.github.io/random.html">Куда-нибудь</a></li>
	    <li><a style="padding: 12px 8px 12px 8px;" rel="next" href="../''' + n_next + \
'''/" accesskey="n">Сюда &gt;</a></li>
	    <li><a style="padding: 12px 8px 12px 8px;" href="http://indiangeogra.github.io">&gt;&gt;</a></li>
	  </div>'''
      
s5 = \
'''	  <br />
	  <br />

          <div id="ComicTitle">
	  <a style="color: #6d6d6d;"
	     href="http://indiangeogra.github.io/archive.html">
	    Архив
	  </a>
	  </div>

	  <footer>

	  <br />'''
      
s_buttons = \
'''	  <center>

	  <!-- I got these buttons from simplesharebuttons.com -->
	  <div id="share-buttons">
	  	<!-- VK -->
     		<a href="http://vkontakte.ru/share.php?url=https://indiangeogra.github.io/''' + args.n + \
'''/" target="_blank">
        		<img src="https://indiangeogra.github.io/vk.png" alt="VK" />
    		</a>
    		<!-- Facebook -->
    		<a href="http://www.facebook.com/sharer.php?u=https://indiangeogra.github.io''' + args.n + \
'''" target="_blank">
		 <img src="https://indiangeogra.github.io/facebook.png" alt="Facebook" />
	        </a>
	        <!-- Twitter -->
		  <a href="https://twitter.com/share?url=https://indiangeogra.github.io/''' + args.n + \
'''/&amp;text=indiangeogra&amp;hashtags=indiangeogra" target="_blank">
        		<img src="https://indiangeogra.github.io/twitter.png" alt="Twitter" />
    		</a>
    	  </div>
'''

s_last = \
'''	  <div style="color: #333">
	  Сослать в наш красный уголок: http://indiangeogra.github.io/''' + args.n + \
'''/index.html<br />
	  Стянуть картинку: http://indiangeogra.github.io/''' + args.n + \
'''/comic.png
	  </div>
	  </center>
        
      </div>
    </div>

    <script src="javascripts/lightbox-plus-jquery.js"></script>
  </body>
</html>
'''

s = s1 + s2 + s3 + s4 + s_buttons + s5 + s_last
f_index = open('index.html', 'w')
f_index.write(s)
f_index.close()