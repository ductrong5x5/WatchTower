import React from 'react'
import pic1 from '../assets/ryan_clayton.jpg'
import pic2 from '../assets/clayton2.jpg'
import pic3 from '../assets/paul.jpg'
import pic4 from '../assets/nerds.jpg'
import logo from '../assets/coolLogo.png'
import {Link} from 'react-router-dom'
import './Home.css'
function Home() {
    var team_pics = [
        pic1,
        pic2,
        pic3,
        pic4
    ]
var image = 0;

const next = () => {
  var slide = document.getElementById("slide");
        image++;
        if(image >= team_pics.length)
        {
            image = 0;
        }
        slide.src = team_pics[image];
}

const prev = () => { 
  var slide = document.getElementById("slide");
  image--;
  if(image < 0)
  {
      image = team_pics.length - 1;
  }
  slide.src = team_pics[image];

} 
    setInterval(next,5000);
  return (
    <div>
        
      <img src={logo}  class = "center" alt="logo"/>
            <h2>
                Watchtower will be a suite of software that enables administrators to
                monitor Linux and Windows system health on a network. The suite will consist
                of a sensor that collects information from connected machines, a backend that stores
                collected information, and one or more user interfaces that allows users to view collected
                information.

            </h2>
            <hr/>
            <h2> 
                Features
            </h2>
            <nav class="nav main-nav">
                <ul>
                    <li>Monitor Systems</li>
                    <li>Agregating Said Data</li>
                    <li>Works as my first web development before I move this all to React!</li>
                </ul>
            </nav>
            <div>
            

            <section class = "header">
                <nav>
                </nav>
            </section>

            </div>
            <hr/>
            <div>
                <h2> About US </h2>
                <ul>
                    <li><button onClick={prev}> Prev </button></li>
                    <li><img id = "slide" src = {pic1}/></li>
                    <li><button class = "leftButton" onClick={next}> Next </button></li>
                </ul>
                <div>
                    <button onclick="window.location.href = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley';" class = "center">
                        Link to our Git Hub!
                    </button>
                </div>
            </div>
            <div>
                <h3> We are a group of computer science majors at UTK trying to survive CS340! In our group we have 2 Claytons, a Duc, Sam, Paul, and Ryan</h3>
            </div>
    </div>
  )
}

export default Home