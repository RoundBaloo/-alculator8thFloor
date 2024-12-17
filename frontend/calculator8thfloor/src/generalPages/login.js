import React, { useState, useEffect } from 'react'
import { Navigate } from 'react-router-dom';
import axios from 'axios';
import { saveToken } from '../calculatorFactPlan/services/tokenService';
import { ApiUrl } from '../apiUrl';
import '../styles/styles.css';
import Logo from '../img/logo.svg';
import SignIn from '../img/sign-in-icon.svg';
import adminService from '../calculatorFactPlan/services/adminService';


const Login = (props) => {
    const api = new ApiUrl()
    const apiUrl = api.getApiUrl()
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [isCorrectLoginData, setIsCorrectLoginData] = useState(true);

    
    useEffect(() => {
        props.setIsLoginPage(true);
        setIsCorrectLoginData(true);
    }, []);


    
    /** Процесс аутентификации */
    const authenticate = () => {
        axios.post(`${apiUrl}/api/token/`, 
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
                props.setIsLoginPage(false);
            })
            .catch(error => {
                console.error(error)
                setIsCorrectLoginData(false);
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
                                style={!isCorrectLoginData ? {borderColor: 'red'} : {}}
                                onChange={(e) => {
                                    setUsername(e.target.value);
                                    setIsCorrectLoginData(true);
                                }}
                            />
                            <input
                                className='password-input' 
                                type='password' 
                                placeholder='Пароль'
                                value={password}
                                style={!isCorrectLoginData ? {borderColor: 'red'} : {}}
                                onChange={(e) => {
                                    setPassword(e.target.value);
                                    setIsCorrectLoginData(true);
                                }}
                            />
                        </div>
                        <button className='sign-in-button' type='button' onClick={authenticate}>
                            <img src={SignIn}></img>
                        </button>
                    </div>
                </div>
            </body>
        </>
    )
}

export default Login;
