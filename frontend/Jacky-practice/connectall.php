<?php

// Connect to MySQL server
$servername = "104.238.215.106";
$username = "root";
$password = "Huffmand3coding";
$conn = mysqli_connect($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


?>