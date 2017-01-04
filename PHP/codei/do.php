<?php
	$data = $_POST['user'];
	@eval("\$ret = $data;"); 
	echo "Hello, ".$ret;
?>