<?php
	// 不显示提示
	error_reporting(0);
	// 设置中文编码
	header("Content-Type:text/html;charset=utf-8");  
	$str1 = $_GET['username'];
	$str2 = $_GET['password'];

	echo "Output:";
	echo "<br / >";
	echo '<h2>Username:</h2>'.$str1;
	echo "<br / >";
	echo '<h2>password:</h2>'.$str2;

	//定义常量  
	define(DB_HOST, 'localhost');  
	define(DB_USER, 'root');  
	define(DB_PASS, '');  
	define(DB_DATABASENAME, 'test');  
	
	$mysqli=new mysqli(DB_HOST,DB_USER,DB_PASS,DB_DATABASENAME);
  	if(!$mysqli){
    	echo "ERROR:".mysqli_connect_error();
    	exit;
 	 }
 	 else{
 	 	echo "<br />"."成功建立连接!"."<br />";
 	 }

 		$conn = mysql_connect(DB_HOST, DB_USER, DB_PASS) or die("connect failed" . mysql_error());  
		mysql_select_db(DB_DATABASENAME, $conn);  
 	 	
		$sql = sprintf("select * from %s where username='%s' and password='%s'", "admin",$str1,$str2);  
		echo $sql;
		$result = mysql_query($sql, $conn);  
		echo '<br>';
		
		if($result){
			echo '<br> SQL Code exe success<br>';
			echo "If no content shows select result is nothing .";
			echo '<table cellpadding="10" border="1">';
			echo '<tr><th>username</th><th>password</th></tr>';
			while($arr=mysql_fetch_array($result)){
				echo "<tr>";
				echo "<td>".$arr[0]."</td>";
				echo "<td>".$arr[1]."</td>";
				echo "</tr>";
        			}
            		echo "</table>";

       		 }
        else{
        	echo "登录失败！！！";
        } 
		
 	
?>