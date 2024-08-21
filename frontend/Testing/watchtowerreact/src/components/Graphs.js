import React, { useState, useEffect } from "react";
import { Chart } from "react-google-charts";
import './Graphs.css';
import Axios from "axios";

function getRandomNumber() {
  return Math.random() * 100;
}


const options = {
  width: "50%",
  height: "50%",
  redFrom: 90,
  redTo: 100,
  yellowFrom: 75,
  yellowTo: 90,
  minorTicks: 5,
};

export function Graph() {
  
  function getData() {
    return [
      ["Label", "Value"],
      ["Memory", getRandomNumber()],
      ["CPU", getRandomNumber()],
      ["Network", getRandomNumber()],
      ["Sams Body count", 100]
    ];
  }
  const [data, setData] = useState(getData);
  const [ID, getID] = useState("");
  useEffect(() => {
    const id = setInterval(() => {
      setData(getData());
    }, 1000);

    return () => {
      clearInterval(id);
    };
  });

  return (

    <div>
        <h1>LOOK AT THIS GRAPH</h1>
        <hr/>
        <Chart
        chartType="Gauge"
        width="100%"
        height="400px"
        data={data}
        options={options}/>
    </div>
  );
}