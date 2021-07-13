<?php

$name = $_POST['name'];
$sport = $_POST['favsport'];

echo "Hi ".$name;

$servername = "localhost";
$username = "nikhil";
$password = "Nikhil*123";
$db = "MateRate";

$conn = new mysqli($servername, $username, $password, $db);

if ($conn->connect_error){
	die("Connection failed: ". $conn->connect_error);
}

$sql = "INSERT INTO SPORTS(name,favsport) values('$name','$sport');";

if ($conn->query($sql) === TRUE) {
	echo "<br>Your favourite sport is recorded as : ".$sport."<br><br>Thank You!";
} else {
	echo "Error: ".$sql."<br>".$conn->error;
}

$conn->close();
?>
