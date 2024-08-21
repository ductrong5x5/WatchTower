<?php
    include 'connectall.php';
?>
<DOCTYPE! html>
    <html>
        <head>
            <title>
                DATA 
            </title>
            
            

            <meta name = "viewport" content ="width=device-width, initial - scale =1">
            <link rel="stylesheet" href="styles.css">
            <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
            <script type="text/javascript">
                google.charts.load('current', {'packages':['gauge']});
                google.charts.setOnLoadCallback(drawChart);

                function drawChart() {

                    var data = google.visualization.arrayToDataTable([
                    ['Label', 'Value'],
                    ['Memory', 80],
                    ['CPU', 55],
                    ['Network', 68]
                    ]);

                    var options = {
                    width: 400, height: 120,
                    redFrom: 90, redTo: 100,
                    yellowFrom:75, yellowTo: 90,
                    minorTicks: 5
                    };

                    var chart = new google.visualization.Gauge(document.getElementById('chart_div'));

                    chart.draw(data, options);

                    // setInterval(function() {
                    // data.setValue(0, 1, 40 + Math.round(60 * Math.random()));
                    // chart.draw(data, options);
                    // }, 13000);
                    // setInterval(function() {
                    // data.setValue(1, 1, 40 + Math.round(60 * Math.random()));
                    // chart.draw(data, options);
                    // }, 5000);
                    // setInterval(function() {
                    // data.setValue(2, 1, 60 + Math.round(20 * Math.random()));
                    // chart.draw(data, options);
                    // }, 26000);
                }

            </script>
        </head>
        <body>
            
            <h2>
               
                <section class = "header">
                    <nav>
                        <div class="nav-links">
                            <a href="watchTower.html"class="hero-btn">Home page</a></li>
                        </div>
                    </nav>
                </section>
                DATA
                
            </h2>
            <?php
                date_default_timezone_set("America/New_York");
                echo "The time is " . date("h:i:s A");
                ?>
            <hr>
            <?php include 'connectall.php';
            $numfetch=1;

            $machine_rows = ($conn ->query("SELECT * FROM machines.machines"))->fetch_assoc();
            
            // $machines_sql = "SELECT * FROM machines.machines";
            // $machines_result = $conn ->query($machines_sql);
            // $machine_rows = $machines_result->fetch_assoc();
           
            // function switchUser($currentUserId, $direction) {
            //     $newUserId = $currentUserId + $direction;
            //     $query = "SELECT id FROM machines WHERE id = $newUserId";
            //     $result = mysqli_query($connection, $query);
            //     // Check if the query returned any results
            //     if (mysqli_num_rows($result) > 0) {
            //         // The previous user ID exists in the database, so update the page with this user's information
            //         // ...
            //     } else {
            //         // The previous user ID does not exist in the database, so do nothing
            //         // ...
            //     }
            // }
            
			?>
            <button onclick="switchUser($ID,+1)">Next User</button>
            <button onclick="switchUser($ID,-1)">Prev User</button>
            
            <h2> 
                User ID: <?php $ID = $machine_rows["id"]; echo $machine_rows["id"]?>
            </h2>
            
            
            <nav class="nav main-nav">
                <ul>
                    <li>System: <?php echo $machine_rows["os_type"]?></li>
                    <li>Version: <?php echo $machine_rows["edition"].'--'.$machine_rows["version_semantic"].'--'.$machine_rows["bitness"]  ?> </li>
                    <li>Timestamp: <?php echo $machine_rows["timestamp"]?></li>
                    <li>CPU : <?php echo $machine_rows["cpu_core_count"].'-core, '.$machine_rows["cpu_thread_count"].'thread'?></li>
                    <li>RAM: <?php $totalram = $machine_rows["ram_installed"]; echo ($machine_rows["ram_installed"]/1024/1024/1024).' GB' ?></li>
                    <?php $GPU_name =  $machine_rows["gpu"]; ?>
                    <li>GPU: <?php echo $machine_rows["gpu"] ?></li>
                    <li>Battery installed:  <?php if ($machine_rows['has_battery'] === "True") echo "Yes (Mobile device)"; else echo "No (Desktop)"; ?></li>
                </ul>
            </nav>
            <hr>
             <!--First part https://www.youtube.com/watch?v=3GsKEtBcGTk -->
            <h2> CPU and RAM</h2>
            <!--Label and table of data -->
            <table>
                
                
                <caption>CPU</caption>
                <tr>
                    <!--Label-->
                    <th>CPU Core </th>
                    <th>CPU Thread </th>
                    <th>CPU_Performance </th>

                </tr>
                <tr>
                    <!--Data to put in -->
                    <td> <?php echo $machine_rows["cpu_core_count"] ?></td>
                    <td> <?php echo $machine_rows["cpu_thread_count"] ?> </td>
                    <?php 
                        $cpu_result=($conn ->query("SELECT * FROM `cpu`.`$ID`"));
                        mysqli_data_seek($cpu_result, $cpu_result->num_rows - 1);
                        $cpu_row = $cpu_result->fetch_assoc(); 
                    ?>
                    <td> <?php echo $cpu_row["percent"] ?> </td>

                </tr>
            </table>
            <!--Div that will hold the pie chart-->
            <!-- <div id="chart_div"></div> -->

           <!--Label and table of data -->
           <table>
               <caption>RAM</caption>
               <tr>
                   <!--Label-->
                   <th>Total Ram </th>
                   <th>Used Ram </th>
                   <th>Available Ram </th>

               </tr>
               
               <tr>
                   <!--Data to put in -->
                   <td> <?php echo $totalram/(1024**3).' GB' ?></td>
                   <?php 
                        $ram_results=($conn ->query("SELECT * FROM `ram`.`$ID`"));
                        mysqli_data_seek($ram_results, $ram_results->num_rows - 1);
                        $ram_row = $ram_results->fetch_assoc(); 
                    ?>
                   <td><?php echo number_format($ram_row["ram_used"]/(1024**3),3) .' GB'?> </td>
                   <td><?php echo  $totalram/(1024**3)  -  number_format($ram_row["ram_used"]/(1024**3),3).' GB' ?></td>

               </tr>
            </table>

            <?php
                $battery_result=($conn ->query("SELECT * FROM `battery`.`$ID`"));
                mysqli_data_seek($battery_result, $battery_result->num_rows - 1);
                $battery_row=$battery_result->fetch_assoc();
            ?>
            <h2> Battery:  <?php echo $battery_row["percentage"].'%' ?> </h2>

            <!-- <table> -->
               <!-- <caption>Battery</caption> -->
               <!-- <tr> -->
                   <!--Label-->
                   <!-- <th>Charge </th> -->
                   <!-- <th>Time left </th> -->
                   <!-- <th>Plugged in </th> -->
               <!-- </tr> -->
               
               <!-- <tr> -->
                   <!--Data to put in -->
                   <!-- <td>data11 </td>
                   <td>data12 </td>
                   <td>data13 </td> -->
               <!-- </tr> -->
            <!-- </table> -->
            <!-- <br> -->

            <h2> GPU : <?php echo $GPU_name ?></h2>
            <?php
                $GPU_result=($conn ->query("SELECT * FROM `gpu`.`$ID`"));
                mysqli_data_seek($GPU_result, $GPU_result->num_rows - 1);
                $GPU_row=$GPU_result->fetch_assoc();
                echo 'VRAM: '.$GPU_row["vram"].' GB';
            ?>
            <!-- <table> -->
               <!-- <caption>System info</caption> -->
               <!-- <tr> -->
                   <!--Label-->
                   <!-- <th>Platform </th> -->
                   <!-- <th>Version </th> -->
                   <!-- <th>Processor </th> -->
                   <!-- <th>Machine </th> -->
               <!-- </tr> -->
               
               <!-- <tr> -->
                   <!--Data to put in -->
                   <!-- <td>data15 </td> -->
                   <!-- <td>data16 </td> -->
                   <!-- <td>data17 </td> -->
                   <!-- <td>data18 </td> -->
               <!-- </tr> -->
            <!-- </table> -->

            <?php
                $net_result=($conn ->query("SELECT * FROM `net`.`$ID`"));
                mysqli_data_seek($net_result, $net_result->num_rows - 1);
                $net_row=$net_result->fetch_assoc();
            ?>
            <h2> Network</h2>
            <table>
               <caption>Network  stats</caption>
               <tr>
                   <!--Label-->
                   <th>Interface </th>
                   <th>RX bytes </th>
                   <th>TX bytes </th>

               </tr>
               <tr>
                   <!--Data to put in -->
                   <td><?php echo $net_row["interface"] ?> </td>
                   <td><?php echo number_format($net_row["rx"]/(1024**3),3) ?> </td>
                   <td><?php echo number_format($net_row["tx"]/(1024**3),3) ?> </td>

               </tr>
            </table>
            <?php
                $net_interface_result=($conn ->query("SELECT * FROM `net_interfaces`.`$ID`"));
                $data_netinter = array();
                while($net_inter_row = $net_interface_result -> fetch_assoc()){
                    $data_netinter[]=array('description' => $net_inter_row["description"],'type' => $net_inter_row["type"],'ip' => $net_inter_row["ip"] );
                } 
                // Create a new array to store the unique values
                $unique_data_netinter = array();

                // Loop through each element of the original array
                foreach ($data_netinter as $net_inter_row) {
                    // Convert the nested array to a string
                    $stringified_net_inter_row = serialize($net_inter_row);
                    
                    // Add the string to the new array
                    $unique_data_netinter[] = $stringified_net_inter_row;
                }
                
                // Remove duplicates from the new array
                $unique_data_netinter = array_unique($unique_data_netinter);
                
                // Create a new array to store the unique nested arrays
                $final_data_netinter = array();

                // Loop through each string in the new array
                foreach ($unique_data_netinter as $stringified_net_inter_row) {
                    // Convert the string back to a nested array
                    $net_inter_row = unserialize($stringified_net_inter_row);
                    
                    // Add the nested array to the new array
                    $final_data_netinter[] = $net_inter_row;
                }
                
                
                // foreach($final_data_netinter as $value)
                // echo $value['description'] . '--' . $value['type'] . '--' . $value['ip'] . "\n";
                // echo "\n";
            
                
            ?>
            <table>
               <caption>Network interface stats</caption>
               <tr>
                   <!--Label-->
                   <th>description </th>
                   <th>type </th>
                   <th>ip </th>

               </tr>
               
                <?php
                    foreach($final_data_netinter as $value)
                        echo "<tr><td>".$value['description'] ."</td><td>" . $value['type'] . "</td><td>". $value['ip'] ."</td></tr>";
                        
                ?>
            <!-- </table>
            <?php
                $contest = mysqli_connect("104.238.215.106","root","Huffmand3coding","test");
                $rows = mysqli_query($contest, "SELECT * FROM tb_data");
            ?>
            <br>
            <table >
                <tr>
                    <td># </td>
                    <td>Name </td>
                    <td>Email </td>
                    <td>Age </td>
                    <td>Country </td>
                </tr>
                <?php foreach($rows as $rows) : ?>
                <tr>
                    <td> <?php echo $rows["#"]; ?> </td>
                    <td> <?php echo $rows["Name"]; ?> </td>
                    <td> <?php echo $rows["Email"]; ?> </td>
                    <td> <?php echo $rows["Age"]; ?> </td>
                    <td> <?php echo $rows["Country"]; ?> </td>
                </tr>
                <?php endforeach; ?>
            </table> -->

        </body>
    </html>
