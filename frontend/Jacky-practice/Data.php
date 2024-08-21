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
          

        </head>
        <body>
            
            <h2> 
               
                <section class = "header">
                    <nav>
                        <div class="nav-links">
                            <a href="watchTower.html"class="hero-btn"><span style="font-size: 35px;">Home page</a></li>
                        </div>
                    </nav>
                </section>
                <!-- <div style="text-align: center; font-size: 100px;background-color: white; display: inline-block;">DATA</div> -->
            </h2>
            <?php
                date_default_timezone_set("America/New_York");
                
                echo '<p style="text-align: right; font-size: 30px;  ">The time is ' . date("h:i:s A") . '</p>';


            ?>
            <div style=";display: flex; justify-content: center">
            
            <div 
                style="width: auto; 
                height: auto; 
                background-color: greenyellow ;
                color: #000 !important; 
                font-size: 100px; 
                text-align: center;
                border-radius: 10px;
                border: 2px solid #000; 
                line-height: 100px; 
                color: #fff;">DATA</div>
            </div>
            <hr style="border-bottom: 30px solid black; ">
            <!-- <?php include 'connectall.php' ?> -->
                <!-- $numfetch=1; -->
                    
                <!-- //$machine_rows = ($conn ->query("SELECT * FROM machines.machines"))->fetch_assoc(); -->
            <div>
            <?php  
                $machines_sql = "SELECT * FROM machines.machines";
                $machines_result = $conn ->query($machines_sql);
                // $machine_rows = $machines_result->fetch_assoc();
			?>
            <?php 
                for ($x = 0; $x <  $machines_result->num_rows; $x++) { ?>
                    <?php $machine_rows = $machines_result->fetch_assoc(); ?>
        
            <div style="display: flex; justify-content: center;">
            <h2 style="font-size: 60px;">User ID: <?php $ID = $machine_rows["id"]; echo $machine_rows["id"]; ?></h2>
            </div>
            <div style="font-size: 60px;text-align: center;">
            <nav class="nav main-nav"><span style="font-size: 35px;">
                <ul>
                    <li>System: <?php echo $machine_rows["os_type"]?></li>
                    <li>Version: <?php echo $machine_rows["edition"].'--'.$machine_rows["version_semantic"].'--'.$machine_rows["bitness"]  ?> </li>
                    <li>Timestamp: <?php echo $machine_rows["timestamp"]?></li>
                    <li>CPU : <?php echo $machine_rows["cpu_core_count"].'-core, '.$machine_rows["cpu_thread_count"].'thread'?></li>
                    <li>RAM: <?php $totalram = $machine_rows["ram_installed"]; echo ($machine_rows["ram_installed"]/1024/1024/1024).' GB' ?></li>
                    <?php $GPU_name =  $machine_rows["gpu"]; ?>
                    <li>GPU: <?php echo $machine_rows["gpu"] ?></li>
                    <li>CPU Clock speed: <?php echo $machine_rows["clock_speed"] ?> </li>
                    <li>Battery installed:  <?php if ($machine_rows['has_battery'] === "True") echo "Yes (Mobile device)"; else echo "No (Desktop)"; ?></li>
                </ul>
            </nav>
            </div>
            <hr >

             <!--First part https://www.youtube.com/watch?v=3GsKEtBcGTk -->
            
            <h2><span style="font-size: 50px;"> CPU, RAM and GPU</h2>
            <div style="display: flex; justify-content: center; gap: 50px;">
            <!--Label and table of data -->
            <table style="width: 700; height: auto; ">
                <caption style="text-align: center;"><span style="font-size: 35px;text-align: center;">CPU</caption>
                <tr>
                    <!--Label-->
                    <th style="width: auto;">CPU Core </th>
                    <th style="width: auto;">CPU Thread </th>
                    <th style="width: auto;">CPU Performance </th>
                    <th style="width: auto;">CPU Clock Speed </th>
                    <th style="width: auto;">CPU Temp </th>

                </tr>
                <tr>
                    <!--Data to put in -->
                    <td style="width: auto;padding: 2px;" ><span style="font-size: 40px;"> <?php echo $machine_rows["cpu_core_count"] ?></td>
                    <td style="width: auto;padding: 2px;"><span style="font-size: 40px;"> <?php echo $machine_rows["cpu_thread_count"] ?> </td>
                    <?php 
                        $cpu_result=($conn ->query("SELECT * FROM `cpu`.`$ID`"));
                        mysqli_data_seek($cpu_result, $cpu_result->num_rows - 1);
                        $cpu_row = $cpu_result->fetch_assoc(); 
                    ?>
                    <td style="width: auto;padding: 2px;"> <span style="font-size: 40px;"><?php echo $cpu_row["percent"]."%" ?> </td>
                    <td style="width: auto;padding: 2px;"> <span style="font-size: 40px;"><?php echo number_format($cpu_row["clock_speed"]/1000,1)."GHz"; ?> </td>
                    <td style="width: auto;padding: 2px;"> <span style="font-size: 40px;"><?php if ($cpu_row["temperature"]>0)echo ($cpu_row["temperature"])."°C"; else echo "N/A" ?> </td>


                </tr>
            </table>
            <!--Div that will hold the pie chart-->
            
            <!-- <div id="chart_div"></div> -->

           <!--Label and table of data -->
           
           <table style="width: auto; height: auto; ">
               <caption style="text-align: center;"><span style="font-size: 35px;">RAM</caption>
               <tr>
                   <!--Label-->
                   <th style="width: auto;">Total Ram </th>
                   <th style="width: auto;">Used Ram </th>
                   <th style="width: auto;">Available Ram </th>
                   <th style="width: auto;">Ram Performance </th>

               </tr>
               
               <tr>
                   <!--Data to put in -->
                   <td style="width: auto;padding: 2px;"> <span style="font-size: 40px;"><?php echo  number_format($totalram/(1024**3),1).' GB' ?></td>
                   <?php 
                        $ram_results=($conn ->query("SELECT * FROM `ram`.`$ID`"));
                        mysqli_data_seek($ram_results, $ram_results->num_rows - 1);
                        $ram_row = $ram_results->fetch_assoc(); 
                    ?>
                   <td style="width: auto;padding: 2px;"><span style="font-size: 40px;"><?php echo number_format($ram_row["ram_used"]/(1024**3),1) .' GB'?> </td>
                   <td style="width: auto;padding: 2px;"><span style="font-size: 40px;"><?php echo  number_format($totalram/(1024**3)  -  $ram_row["ram_used"]/(1024**3),1).' GB' ?></td>
                   <td style="width: auto;padding: 2px;"> <span style="font-size: 40px;"><?php echo  number_format(($ram_row["ram_used"] /$totalram )*100,1).' %' ?></td>
               </tr>
            </table>
            <?php
                $GPU_result=($conn ->query("SELECT * FROM `gpu`.`$ID`"));
                mysqli_data_seek($GPU_result, $GPU_result->num_rows - 1);
                $GPU_row=$GPU_result->fetch_assoc();
               
            ?>
            <table style="width: 450; height: auto; ">
               <caption style="text-align: center;"><span style="font-size: 35px;">GPU</caption>
               <tr>
                   <!--Label-->
                   <th style="width: auto;">VRAM </th>
                   <th style="width: auto;">Frequency </th>
                   <th style="width: auto;">Temperature </th>

               </tr>
               
               <tr>
                   <!--Data to put in -->
                   <td style="width: auto;padding: 2px;"> <span style="font-size: 40px;"><?php echo number_format($GPU_row["vram"]/(1024**2), 2).' GB' ?></td>
                   <td style="width: auto;padding: 2px;"><span style="font-size: 40px;"><?php if($GPU_row["frequency"]>0) echo $GPU_row["frequency"]; else echo "N/A";?> </td>
                   <td style="width: auto;padding: 2px;"><span style="font-size: 40px;"><?php if($GPU_row["temperature"]>0) echo ($GPU_row["temperature"])."°C"; else echo "N/A"; ?></td>

               </tr>
            </table>
            </div>
            
            <h2><span style="font-size: 50px;"> Disk </h2>
            <div style="display: flex; justify-content: center; gap: 50px;">
            <?php $disk_result=($conn ->query("SELECT * FROM `disks`.`$ID` order by type"));
                $disk_allrow=array();
                while($disk_row = $disk_result-> fetch_assoc()){
                    $disk_allrow[]=array('disk' => $disk_row["disk"],'type' => $disk_row["type"],'capacity' => $disk_row["capacity"],'used' => $disk_row["used"],'removable' => $disk_row["removable"] );
                }
            ?>
            <table style="width: 1000; height: auto; ">
               <caption style="text-align: center;"><span style="font-size: 35px;">Disk Information</caption>
               <tr>
                   <!--Label-->
                   <th style="width: auto;">Disk </th>
                   <th style="width: auto;">Type </th>
                   <th style="width: auto;">Capacity </th>
                   <th style="width: auto;">Used </th>
                   <th style="width: auto;">Used percent </th>
                   <th style="width: auto;">Removable </th>

               </tr>
               <?php
                    foreach($disk_allrow as $value1) {
                        echo "<tr>
                                <td><span style='font-size:40px;'>".$value1['disk']."</span></td>
                                <td><span style='font-size:40px;'>".$value1['type']."</span></td>
                                <td><span style='font-size:40px;'>".number_format($value1['capacity']/(1024**3),1).' GB'."</span></td>
                                <td><span style='font-size:40px;'>".number_format($value1['used']/(1024**3),1).' GB'."</span></td>
                                <td><span style='font-size:40px;'>".number_format(($value1['used']/$value1['capacity'])*100,1).' %'."</span></td>";
                                if ($value1['removable'] == "False") {
                                    echo "<td style='width:auto;'><span style='font-size:30px;color:red;'>".'No'."</span></td>";
                                } else {
                                    echo "<td style='width:auto;'><span style='font-size:30px;color:green;'>".'Yes'."</span></td>";
                                }
                        echo "</tr>";
                    }
                ?>


               
            </table>
            </div>
            <?php
                $battery_result=($conn ->query("SELECT * FROM `battery`.`$ID`"));
                mysqli_data_seek($battery_result, $battery_result->num_rows - 1);
                $battery_row=$battery_result->fetch_assoc();
            ?>
            <h2><span style="font-size: 50px;"> Battery:  <?php if($battery_row["percentage"]>100){echo "100" . "% (This is a Desktop - no battery)";} else echo $battery_row["percentage"].'% (Mobile device)';  ?> </h2>

            <?php
                // $net_result=($conn ->query("SELECT * FROM `net`.`$ID`"));
                // mysqli_data_seek($net_result, $net_result->num_rows - 1);
                // $net_row=$net_result->fetch_assoc();

                $query = "SELECT * FROM net.`$ID` WHERE `$ID`.timestamp = (SELECT max(timestamp) from net.`$ID`) order by description";
                $net_result=mysqli_query($conn, $query);
                
            ?>
            <h2> <span style="font-size: 50px;">Network</h2>

            <?php

                mysqli_fetch_all($net_result, MYSQLI_ASSOC);
            
            ?>
            <div style="display: flex; justify-content: center; gap: 50px;">
            <table style="width: auto; height: auto; ">
            <caption style="text-align: center;"><span style="font-size: 20px;">Network Interface</caption>
               <tr>
                   
                   <th >MAC </th>
                   <th >Name </th>
                   <th >Description </th>
                   <th >Type </th>
                   <th >IP </th>
                   <th >RX </th>
                   <th >TX </th>


               </tr>
               
                <?php
                    foreach($net_result as $value)
                        echo "<tr>
                            <td>".$value['mac'] ."</td>
                            <td>".$value['name'] . "</td>
                            <td>".$value['description'] ."</td>
                            <td>".$value['net_type'] ."</td>
                            <td>".$value['ip'] . "</td>
                            <td>".number_format($value['rx']/(1024**2),1).' MB' ."</td>
                            <td>".number_format($value['tx']/(1024**2),1).' MB' ."</td>
                        
                        
                        </tr>";
                        
                ?>
            </table>
            </div>
            <br>
            <hr style="border-bottom: 10px dashed  black; ">
            <?php } ?>
            </div>
        </body>
    </html>
