import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App1 from './App';
import Login from './generalPages/login'
import InputData from './calculatorFactPlan/inputData';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter as Router, Routes, Link, Route } from 'react-router-dom';


function App () {

  return (
    <Router>
      <>
        <header>
          <nav>
            <ul>
              <Link to='/calculatorFactPlan'><button type='button'>xxx</button>
              </Link>
              <Link to='/pupu1'>
              </Link>
              <Link to='/pupu2'>
              </Link>
            </ul>
          </nav>
        </header>
        <Routes>
          <Route exact path="/" element={<Login />} />
          <Route exact path="/calculatorFactPlan" element={<App1 />} />
          <Route exact path="/inputForCalculatorFactPlan" element={<InputData />} />
        </Routes>
      </>
    </Router>
  );

}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
