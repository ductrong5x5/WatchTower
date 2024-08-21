const express = require("express");
const app = express();
const mysql = require("mysql2");

const db = mysql.createConnection({
    user: "root",
    host: "104.238.215.106",
    password: "Huffmand3coding",
    database: "machines"
});

db.connect(function (err) {
  if (err) throw err;
  console.log('Connected to MySQL database');
});

app.get('/Graphs', function (req, res) {
    connection.query('SELECT * FROM machines.machines', function (error, results) {
      if (error) throw error;
      res.send(results);
    });
  });

app.listen(3002, () => {
    console.log('Conected!');
})









