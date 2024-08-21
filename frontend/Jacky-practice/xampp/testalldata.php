
<?php
include 'connectall.php';

// Get list of databases
$sql = "SHOW DATABASES";
$result = $conn->query($sql);
// Loop through each database and do something
if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        $database_name = $row["Database"];
        echo "Database: " . $database_name . "<br>";
        // Do something with this database
        // For example, you can list all tables in this database
        $sql2 = "SHOW TABLES IN " . $database_name;
        $result2 = $conn->query($sql2);
        if ($result2->num_rows > 0) {
            while($row2 = $result2->fetch_assoc()) {
                $table_name = $row2["Tables_in_" . $database_name];
                echo "Table: " . $table_name . "<br>";
            }
        } else {
            echo "0 tables in " . $database_name;
        }
}
} else {
    echo "0 databases";
}

// Close MySQL connection
$conn->close();

?>
