<?php
$handle = fopen("test.txt","w");//write in test.txt file
extract($_POST);//to get all the contents received using POST method
if (fwrite($handle, $url) === FALSE) {
        echo "Cannot write to file ";
        exit;
    }
	
//to retrieve from server in the form of json
header('Content-type: application/json');
echo json_encode($url);

fclose($handle);
?>