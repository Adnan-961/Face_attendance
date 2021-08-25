<!DOCTYPE html>
<?php
   include('session.php');
?>
<html lang = "en-US">
 <head>
 <script type = "text/JavaScript">
         <!--
            function AutoRefresh( t ) {
               setTimeout("location.reload(true);", t);
            }
         //-->
      </script>
<link rel="stylesheet" href="style.css?v=<?php echo time(); ?>">
 <meta charset = "UTF-8">
 <title>Student Attendance</title>
 </head>
 <body onload = "JavaScript:AutoRefresh(3000);">
 
<div>
		<a href="exportpdf.php" download><span>Download</span><span>PDF</span></a>
		<a href="exportxls.php" download><span>Download</span><span>XLS</span></a>
</div>
<h1 align="center">Welcome <?php echo $login_session; ?></h1> 
 <p>
 <?php
  try {
  $con= new PDO('mysql:host=localhost;dbname=student_db', "root", "");
  $con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  $query = "SELECT id as 'ID' , first_name as 'First Name',last_name as 'Last Name' ,major as 'Major',date as 'Date', is_attendant as 'Present',timestamp as 'AT' FROM attendance ORDER BY date ASC,id,First_name";
  //first pass just gets the column names
  print "<table> ";
  $result = $con->query($query);
  //return only the first row (we only need field names)
  $row = $result->fetch(PDO::FETCH_ASSOC);
  print " <tr> ";
  foreach ($row as $field => $value){
   print " <th>$field</th> ";
  } // end foreach
  print " </tr> ";
  //second query gets the data
  $data = $con->query($query);
  $data->setFetchMode(PDO::FETCH_ASSOC);
  foreach($data as $row){
   print " <tr> ";
   foreach ($row as $name=>$value){
   print " <td>$value</td> ";
   } // end field loop
   print " </tr> ";
  } // end record loop
  print "</table> ";
  
  } catch(PDOException $e) {
   echo 'ERROR: ' . $e->getMessage();
  } // end try
 ?>
 </p>

      <h2><a href = "logout.php"><span>Signout</span><span>Signout</span></a></h2>
	  
 </body>
</html>