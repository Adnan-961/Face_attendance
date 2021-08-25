<?php
   include('config.php');
   session_start();
   $user_check = $_SESSION['login_user'];
   
   $ses_sql = mysqli_query($db,"SELECT username FROM instructors WHERE username='$user_check' UNION SELECT username FROM admin WHERE username='$user_check' UNION SELECT username FROM students WHERE username='$user_check'
");
   
   $row = mysqli_fetch_array($ses_sql,MYSQLI_ASSOC);
   
   $login_session = $row['username'];
   
   if(!isset($_SESSION['login_user'])){
      header("location:login.php");
      die();
   }
?>