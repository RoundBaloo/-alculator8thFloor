import React, { useState } from 'react'
import { Navigate } from 'react-router-dom';
import axios from 'axios';
import { saveToken } from '../calculatorFactPlan/services/tokenService';
import { ApiDirectory } from '../apiDir';
import '../styles/styles.css';
import Logo from '../img/logo.svg';
import SignIn from '../img/sign-in-icon.svg';
import adminService from '../calculatorFactPlan/services/adminService';


const Login = (props) => {
    const api = new ApiDirectory()
    const apiDir = api.getApiUrl()
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    const authenticate = () => {
        // const inputData = {
        //   "username": "a@a.com",
        //   "password": "12345",
        // };
    
        axios.post(`${apiDir}/api/token/`, 
            JSON.stringify({
                "username": `${username}`,
                "password": `${password}`,
            }), 
            {
                headers: {
                'Content-Type': 'application/json'
                }
            })
            .then(response => {
                saveToken(response.data.access)
                setIsAuthenticated(true)
                props.updateIsAdmin(response.data.role == 'admin' ? true : false)
                adminService.setAdmin(response.data.role == 'admin' ? true : false);
            })
            .catch(error => {
                console.error('ABOBA ERROR')
            })
    }

    if (isAuthenticated) {
        return <Navigate to='/inputForCalculatorFactPlan' />
    }

    return (
        <>
            <body>
                <div className='login-page'>
                    <div className='login-header'>
                        <img src={Logo} width="50" height="50"></img>
                    </div>

                    <div className='input-form'>
                        <div className='login-and-password'>
                            <input 
                            className='login-input'
                            placeholder='Логин' 
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            />
                            <input
                            className='password-input' 
                            type='password' 
                            placeholder='Пароль'
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            />
                        </div>
                        <button className='sign-in-button' type='button' onClick={authenticate}><img src={SignIn}></img></button>
                    </div>
                </div>
            </body>
        </>
    )
}

export default Login;
