<DOCTYPE! html>
<html lang="en" dir="ltr">
	<head>
		<meta charset = "utf-8">
		<title>Watchtower</title>

	</head>
	<body >
		
		
		<script type="text/javascript">
			// <canvas id="myChart" style="width:100%;max-width:700px"></canvas>
			function table(){
				
				const xhttp = new XMLHttpRequest();
				xhttp.onload =function(){
					document.getElementById("table").innerHTML = this.responseText;
				}
				xhttp.open("GET","data.php");
				xhttp.send();
			}
			setInterval(function(){table();},1000);
			
			
		</script>
		
		
		<div id ="table"></div>
	</body>
</html>