<?php
$servername = "localhost";
$username = "myqslUser";
$password = "giveMeAccess";
$dbname = "Scores";

echo $servername " , " $username " , " $password " , " $dbname

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO Board (name, score)
VALUES ('{$_POST["name"]}','{$_POST["score"]}')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
