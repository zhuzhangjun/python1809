<?php
//http://127.0.0.1/hangowa/php/register.php
header('Access-Control-Allow-Origin: *');
header("Content-Type: text/html; charset=utf8");
//接收到前端提交过来的参数
@$username = $_POST["username"];
@$pwd = $_POST["pwd"];
@$mailbox = $_POST["mailbox"];

//连接数据库MySql
$conn = new mysqli("127.0.0.1", "root", "", "usertable") or die("连接失败");

//判断用户名是否已经存在
$sql = "select * from user where username='$username'";
$result = $conn->query($sql);
if ($result && $result->num_rows>0) {
    $arr = array("status"=>0, "msg"=>"用户名已经存在");
    echo  json_encode($arr);
}
else {
    //插入数据， 注册
    $sql = "insert into user(username, password, mailbox) values('$username', '$pwd', '$mailbox')";
    $result = $conn->query($sql);
    if ($result) {
        $arr = array("status"=>1, "msg"=>"注册成功");
        echo  json_encode($arr);
    } else {
        $arr = array("status"=>0, "msg"=>"注册失败");
        echo  json_encode($arr);
    }
}
$conn->close();
?>