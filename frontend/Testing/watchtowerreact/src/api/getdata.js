import axios from 'axios';
import React from 'react'
function fetchData() {
    axios.get('http://localhost:3002/api/data')
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }

  
  function getdata() {
    useEffect(() => {
        fetchData();
      }, []);
    
      return (
        <div>
            
        </div>
      )
  }
  
  export default getdata
  