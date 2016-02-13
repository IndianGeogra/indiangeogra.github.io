<?php
$urls = array("http://indiangeogra.github.io/1", 
              "http://indiangeogra.github.io/2"); 
$url = $urls[array_rand($urls)]; 
header("Location: http://$url"); 
?>
