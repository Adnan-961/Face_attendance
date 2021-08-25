<?Php
$host_name = "localhost";
$database = "db_name"; // Change your database nae
$username = "";          // Your database user id 
$password = "";          // Your password

//////// Do not Edit below /////////
try {
$dbo = new PDO('mysql:host='.$host_name.';dbname='.$database, $username, $password);
} catch (PDOException $e) {
print "Error!: " . $e->getMessage() . "<br/>";
die();
}
?>