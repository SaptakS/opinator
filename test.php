<?php
$handle = fopen("test.txt","w");
extract($_POST);
if (fwrite($handle, $url) === FALSE) {
        echo "Cannot write to file ";
        exit;
    }

echo "Success";

fclose($handle);
?>