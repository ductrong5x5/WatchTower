<!DOCTYPE html>
<html>
	<title>
		<head> Fetchdata </head>
	</title>
	<body>
	<table align ="center" border="1px" style ="width:600px; line-height:40px;">
		<tr>
			<th colspan="4"><h2> Machine </h2> </th>
		</tr>
		<t>
			<th> timestamp </th>
			<th> id	</th>
			<th> percentage </th>
		</t>

		<?php
			$conn=mysqli_connect("104.238.215.106","root","Huffmand3coding","battery");
			$sql = "SHOW TABLES";
			$result = mysqli_query($conn, $sql);
			while ($table_row = mysqli_fetch_array($result)) {
				$table_name = $table_row[0];
				$table_sql = "SELECT * FROM battery.`$table_name`";
				$table_result = $conn ->query($table_sql);
				mysqli_data_seek($table_result, $table_result->num_rows - 1);
				$row = $table_result->fetch_assoc();
				echo "<tr><td>".$row["timestamp"] . "</td><td>".$row["id"]. "</td><td>".$row["percentage"];
				
			}
			//echo $row["timestamp"];
			mysqli_close($conn);
		?>
		</table>
	</body>
</html>



