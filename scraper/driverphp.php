<?php
$command = escapeshellcmd ('/var/www/html/opinator/scraper/scrapydriver.py');
$pID = (string)($_POST['product_code']);
$command = $command." ".$pID;
//die($command);
$output = shell_exec ($command);
//echo $output;
$command2 = escapeshellcmd ('python /var/www/html/opinator/mindwrap/sentiment.py');
$output2 = shell_exec ($command2);
echo $output2
#
#Run corenlp code here
#and get the output in $sentiment
#using shell_exec execute the store_in_db.py with $sentiment and $pID as command line argument
#This is just for the sake of updating the database.
#according to the $sentiment pass the right sentiment to the user.
#
?>
