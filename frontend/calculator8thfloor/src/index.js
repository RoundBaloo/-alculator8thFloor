import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Login from './generalPages/login'
import InputData from './calculatorFactPlan/inputData';
import CalculatorFactPlanTable from './calculatorFactPlan/calculatorFactPlanTable';
import HeadPermissions from './calculatorFactPlan/headPermissions';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './styles/styles.css'


function App() {
  const [isAdmin, setIsAdmin] = useState(false);
  const [currentCalculator, setCurrentCalculator] = useState('calculatorFactPlan')

  const updateIsAdmin = (admin) => {
    setIsAdmin(admin);
  }

  return (
    <Router>
      <>
          <Routes>
            <Route exact path="/" element={<Login updateIsAdmin={updateIsAdmin} />} />
            <Route exact path="/calculatorFactPlan" element={<CalculatorFactPlanTable isAdmin={isAdmin}
                                                                                      currentCalculator={currentCalculator}
                                                                                      setCurrentCalculator={setCurrentCalculator} />} />
            <Route exact path="/inputForCalculatorFactPlan" element={<InputData currentCalculator={currentCalculator}
                                                                                setCurrentCalculator={setCurrentCalculator} />} />
            <Route exact path="/handleUsersPermisions" element={<HeadPermissions currentCalculator={currentCalculator}
                                                                                  setCurrentCalculator={setCurrentCalculator}/>} />
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
