<?php
$json = $_POST['json'];
 if (json_decode($json) != null) { /* sanity check */
     $file = fopen('data.json','w+');
     fwrite($file, $json);
     fclose($file);
	 echo $json;
   } else {
     // handle error
		echo "No URL";
   }
?>