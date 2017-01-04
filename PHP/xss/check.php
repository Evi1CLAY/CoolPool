<?php
	// 设置 测试 cookie
	setcookie("user", "anka9080", time()+3600);

	echo '<center>Message:<br>';

	echo $_GET['username']."</center>";
?>