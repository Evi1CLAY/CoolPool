<?php
/**
 * Created by 独自等待
 * Date: 14-1-22
 * Time: 下午7:19
 * Name: upload1.php
 * 独自等待博客：http://www.waitalone.cn/
 */
//文件上传漏洞演示脚本之js验证
$uploaddir = 'uploads/';
if (isset($_POST['submit'])) {
    if (file_exists($uploaddir)) {
        if (move_uploaded_file($_FILES['upfile']['tmp_name'], $uploaddir . '/' . $_FILES['upfile']['name'])) {
            echo 'upload success, Save at ：' . $uploaddir . $_FILES['upfile']['name'] . "\n";
        }
    } else {
        exit($uploaddir . ' dir not exists,please create first');
    }
    //print_r($_FILES);
}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>
    <meta http-equiv="content-language" content="zh-CN"/>
    <!-- JS验证实例 -->
    <title>文件上传漏洞演示</title>
    <script type="text/javascript">
        function checkFile() {
            var file = document.getElementsByName('upfile')[0].value;
            if (file == null || file == "") {
                alert("你还没有选择任何文件，不能上传!");
                return false;
            }
            //定义允许上传的文件类型
            var allow_ext = ".jpg|.jpeg|.png|.gif|.bmp|";
            //提取上传文件的类型
            var ext_name = file.substring(file.lastIndexOf("."));
            //alert(ext_name);
            //alert(ext_name + "|");
            //判断上传文件类型是否允许上传
            if (allow_ext.indexOf(ext_name + "|") == -1) {
                var errMsg = "该文件不允许上传，请上传" + allow_ext + "类型的文件,当前文件类型为：" + ext_name;
                alert(errMsg);
                return false;
            }
        }
    </script>
<body>
<h3>文件上传漏洞演示</h3>

<form action="" method="post" enctype="multipart/form-data" name="upload" onsubmit="return checkFile()">
    <input type="hidden" name="MAX_FILE_SIZE" value="204800"/>
    请选择要上传的文件：<input type="file" name="upfile"/>
    <input type="submit" name="submit" value="上传"/>
</form>
</body>
</html>