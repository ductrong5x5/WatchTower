<DOCTYPE! html>
    <html>
        <head>
            <title>
                Watchtower
            </title>
            <meta name = "viewport" content ="width=device-width, initial - scale =1">
            <link rel="stylesheet" href="styles1.css">
            <script src="https://www.gstatic.com/charts/loader.js"></script>
            <script type="text/javascript">
                google.charts.load("current", {packages:["corechart"]});
                google.charts.setOnLoadCallback(drawChart);
                function drawChart() {
                  var data = google.visualization.arrayToDataTable([
                    ["Proccesses", "Second", { role: "style" } ],
                    ["i7-700k", 198765, "#b87333"],
                    ["AMD-9000", 73891, "silver"],
                    ["Made-Up Proccessor", 999999, "gold"],
                  ]);
            
                  var view = new google.visualization.DataView(data);
                  view.setColumns([0, 1,
                                   { calc: "stringify",
                                     sourceColumn: 1,
                                     type: "string",
                                     role: "annotation" },
                                   2]);
            
                  var options = {
                    title: "Proccess Per Second",
                    width: 600,
                    height: 300,
                    bar: {groupWidth: "95%"},
                    legend: { position: "none" },
                    backgroundColor: {fill: "white"},
                  };
                  var chart = new google.visualization.BarChart(document.getElementById("barchart_values"));
                  chart.draw(view, options);
              }
              </script>
            <script>
                var team_pics = [
                    './ryan_clayton.jpg',
                    './sui.jpg',
                    'paul.jpg',
                    'clayton2.jpg'
                ]
                var image = 0;
                function next() {
                    var slide = document.getElementById("slide");
                    image++;
                    if(image >= team_pics.length)
                    {
                        image = 0;
                    }
                    slide.src = team_pics[image];
                }

            </script>
        </head>
        <body>
            <div class = "section cc-home-wrap">
                <div class = "intro-header">
                    <div class = " intro-content cc-homepage">
                        <div class = "heading-jumbo">WatchTower</div>
                        <div class = "paragraph-bigger">System Monitoring Application<br></div>
                    
                    <a href="Data.php" class = "button cc-jumbo-button ">
                        <div>Data</div>
                    </a>
                </div>
                </div>
            </div>
            <div class = "container">
                <div class = "motto-wrap"></div>
                <div class = "divider"></div>
                <div class = "home-content-wrap">
                    <div class = "home-section-wrap">
                        <div class = "label cc-light">About</div>
                        <h2 class = "section-heading">Who we are</h2>
                        <p class = "paragraph-light">  We are a group of computer science majors at UTK trying to survive CS340! In our group we have 2 Claytons, a Duc, Sam, Paul, and Ryan.  
                            We have created a system monitoring application that will have a program that will monitor the specs of machines running Linux, Mac OS, & Windows and send the information to a mySQL database to be fetched by this website!
                        </p>
                    </div>
                    <a class = "button w-inline-block" onclick="next()">Next</a>
                    <br>
                    <div><img  id = "slide" src = "./ryan_clayton.jpg" alt=""></div>
                </div>
            </div>
            <div class = "divider"></div>
        </body>
    </html>
