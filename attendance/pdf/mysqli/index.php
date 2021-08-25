<!doctype html public "-//w3c//dtd html 3.2//en">
<html>
<head>
<title>plus2net PDF document with MySQL data</title>
<link rel="stylesheet" href="style.css" type="text/css">
</head>
<body>
<?Php
////////////////
require "config.php"; // Database connection details. 


$count="select * from student LIMIT 0,10";

echo "<table>";
echo "<tr><th>id</th><th>name</th><th>class</th><th>mark</th><th>Sex</th></tr>";
if ($result_set = $connection->query($count)) {
while($row = $result_set->fetch_array(MYSQLI_ASSOC)){
echo "<tr ><td>$row[id]</td><td>$row[name]</td><td>$row[class]</td><td>$row[mark]</td><td>$row[sex]</td></tr>";
}
echo "</table>";
$result_set->close();
}

?>
<br><br> If you are seeing the student list above then your database connection, installation of table are working fine.<br><br>
Now you can check the <a href=index-pdf.php>generated PDF list</a> . 
<br><br>
You can check the <a href=index1-pdf.php>generated PDF List with link to mark sheet</a>. 

<br><br><br>Read Tutorial at <br>
<a href=https://www.plus2net.com/php_tutorial/pdf-data-student.php rel='nofollow'>PDF Generation using MySQL data from plus2net.com</a>

</body>
</html>
