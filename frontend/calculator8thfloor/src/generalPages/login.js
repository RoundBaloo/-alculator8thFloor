import React, { useState } from 'react'
import { Navigate } from 'react-router-dom';
import axios from 'axios';
import { saveToken } from '../tokenService';


const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    const authenticate =() => {
        // const inputData = {
        //   "username": "a@a.com",
        //   "password": "12345",
        // };
    
        axios.post('http://127.0.0.1:8000/api/token/', 
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
        {/* <Link to='/calculatorFactPlan'> */}
            <button type='button' onClick={authenticate}>Войти в айти</button>
        {/* </Link> */}
    </>
    )
}

export default Login;
