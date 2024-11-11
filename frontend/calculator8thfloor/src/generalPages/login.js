import React, { useState } from 'react'
import { Navigate } from 'react-router-dom';
import axios from 'axios';
import { saveToken } from '../tokenService';
import { ApiDirectory } from '../apiDir';
import '../styles/styles.css';


const Login = () => {
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
                console.log(response.data.access)
                saveToken(response.data.access)
                setIsAuthenticated(true)
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
            <input 
            className='aboba'
            placeholder='login' 
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            />
            <input 
            type='password' 
            placeholder='password'
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            />
            <button type='button' onClick={authenticate}>Войти в айти</button>
        </>
    )
}

export default Login;
