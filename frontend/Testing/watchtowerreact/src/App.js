import './App.css';
import Home from './components/Home';
import {Graph} from './components/Graphs';
import MyButton from './button/Button';
import { BrowserRouter as Router, Routes, 
  Route } from "react-router-dom";
function App() {

  
  return (
    <div className="App">
             <Router>
             <MyButton to="" />
             <MyButton to="Graphs"/>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/Graphs" element={<Graph />} />
                </Routes>
            </Router>
    </div>
  );
}

export default App;