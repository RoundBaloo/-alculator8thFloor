import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Login from './generalPages/login'
import InputData from './calculatorFactPlan/inputData';
import CalculatorFactPlanTable from './calculatorFactPlan/calculatorFactPlanTable';
import HeadPermissions from './calculatorFactPlan/headPermissions';
import Calculator1 from './calculator1/calculator1';
import Calculator2 from './calculator2/calculator2';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './styles/styles.css'
import Logo from './img/logo.svg'
import { Link } from 'react-router-dom';
import adminService from './calculatorFactPlan/services/adminService';
import { removeToken } from './calculatorFactPlan/services/tokenService';


function App() {
  const [isAdmin, setIsAdmin] = useState(false);
  const [currentCalculator, setCurrentCalculator] = useState('calculatorFactPlan')
  const [isLoginPage, setIsLoginPage] = useState(false);

  const updateIsAdmin = (admin) => {
    setIsAdmin(admin);
  }

  return (
    <Router>
      <>
        {!isLoginPage && (
          <header>
          <nav className='inputData-navigation'>
              <img src={Logo} width="50" height="50" style={{ marginRight: "78px" }}></img>
              <ul className={'headerButtons'}>
                  <Link to='/calculatorFactPlan'>
                      <button
                          className={`calculator-type-button ${currentCalculator !== 'calculatorFactPlan' ? 'nav-calculator-type-button' : ''}`}
                          type='button'
                          onClick={() => setCurrentCalculator('calculatorFactPlan')}>1 калькулятор
                      </button>
                  </Link>
                  <Link to='/calculator1'>
                      <button
                          className={`calculator-type-button ${currentCalculator !== 'calculator1' ? 'nav-calculator-type-button' : ''}`}
                          type='button'
                          onClick={() => setCurrentCalculator('calculator1')}>2 калькулятор
                      </button>
                  </Link>
                  <Link to='/calculator2'>
                      <button
                          className={`calculator-type-button ${currentCalculator !== 'calculator2' ? 'nav-calculator-type-button' : ''}`}
                          type='button'
                          onClick={() => setCurrentCalculator('calculator2')}>3 калькулятор
                      </button>
                  </Link>
                  {adminService.getAdmin() && (
                            <Link to='/handleUsersPermisions'>
                                <button className='calculator-type-button' type='button'>Управление доступом</button>
                            </Link>
                        )}
                  <Link to='/'>
                      <button
                          className={`calculator-type-button`}
                          type='button'
                          onClick={() => {
                            removeToken();
                            adminService.clearAdminStatus();
                          }}>Выйти из аккаунта
                      </button>
                  </Link>
              </ul>
          </nav>
        </header>
        )}
        <Routes>
          <Route exact path="/" element={<Login updateIsAdmin={updateIsAdmin} 
                                                setIsLoginPage={setIsLoginPage} />} />
          <Route exact path="/calculatorFactPlan" element={<CalculatorFactPlanTable isAdmin={isAdmin}
                                                                                    currentCalculator={currentCalculator}
                                                                                    setCurrentCalculator={setCurrentCalculator} />} />
          <Route exact path="/inputForCalculatorFactPlan" element={<InputData currentCalculator={currentCalculator}
                                                                              setCurrentCalculator={setCurrentCalculator} />} />
          <Route exact path="/handleUsersPermisions" element={<HeadPermissions currentCalculator={currentCalculator}
                                                                                setCurrentCalculator={setCurrentCalculator}/>} />
          <Route exact path="/calculator1" element={<Calculator1 />} />
          <Route exact path="/calculator2" element={<Calculator2 />} />
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
