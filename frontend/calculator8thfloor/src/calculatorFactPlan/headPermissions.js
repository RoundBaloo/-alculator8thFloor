import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { getToken } from '../tokenService';
import { Link } from 'react-router-dom';


const createUser = (token, createUserInformatiom, getUsersFunction) => {
    axios.post('http://127.0.0.1:8000/head/',
        JSON.stringify({
            "username": `${createUserInformatiom.username}`,
            "email": `${createUserInformatiom.email}`,
            "password": `${createUserInformatiom.password}`,
        }),  {
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        console.log('пользователи загружены')
        getUsersFunction();
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
}


export default function HeadPermissions() {
    const token = getToken();
    const [users, setUsers] = useState();
    const [isLoading, setIsLoading] = useState(false);
    const [username, setUsername] = useState();
    const [email, setEmail] = useState();
    const [password, setPassword] = useState();
    const [confirmedPassword, setConfirmedPassword] = useState();


    const getUsers = () => {
        setIsLoading(true);
        axios.get('http://127.0.0.1:8000/head/', {
            headers: {
                'Authorization': `Bearer ${token}`,
            }
        })
        .then(response => {
            console.log('пользователи загружены')
            setUsers(response.data);
            setIsLoading(false);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            setIsLoading(false);
        });
    };


    useEffect(() => {
        getUsers();
    }, []);


    const renderUsers = () => {
        if (users) {
            return (
                <div className="users">
                    <h3>Users:</h3>
                    <ul>
                        {users.map((user) => (
                            <li key={user.id}>
                                <strong>Username:</strong> {user.username} <br />
                                <strong>Email:</strong> {user.email}
                            </li>
                        ))}
                    </ul>
                </div>
            ); 
        } else {
            return (
                <div className="text-center">
                    <div className="spinner-border" role="status">
                        <span className="sr-only">Loading...</span>
                    </div>
                </div>
            );
        }
    };


    return (
        <>
            <div className="register">
                <input type='text' placeholder='username' onChange={e => (setUsername(e.target.value))} />
                <input type='email' placeholder='email' onChange={e => (setEmail(e.target.value))} />
                <input type='password' placeholder='password' onChange={e => (setPassword(e.target.value))} />
                <input type='password' placeholder='confirm password' onChange={e => (setConfirmedPassword(e.target.value))} />
                <button type='button' onClick={() => {
                    createUser(token, {
                        "username": username,
                        "email": email,
                        "password": password,
                    }, 
                getUsers);
                }}>добавить</button>
            </div>
            { renderUsers() }
            <Link to='/calculatorFactPlan'>
                <button type='button'>назад</button>
            </Link>
        </>
    )
}
