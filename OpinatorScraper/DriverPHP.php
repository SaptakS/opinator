<?php
$command = escapeshellcmd ('/home/vivek/WebScrapping/OpinatorScraper/Driver.py');
$pID = (string)1473605202;
$command = $command." ".$pID;
$output = shell_exec ($command);
echo $output;
?>
