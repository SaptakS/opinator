<?php
$command = escapeshellcmd ('/home/vivek/OpinatorScraper/OpinatorScraper/ScrapyDriver_AmazonSpider.py');
$pID = (string)1473605202;
$command = $command." ".$pID;
$output = shell_exec ($command);
echo $output;
?>
