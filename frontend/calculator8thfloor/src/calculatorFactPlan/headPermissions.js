import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { getToken } from '../tokenService';
import { Link } from 'react-router-dom';
import { ApiDirectory } from '../apiDir';
import '../styles/styles.css';


const createUser = (token, createUserInformatiom, getUsersFunction, apiDir) => {
    axios.post(`${apiDir}/head/`,
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
        getUsersFunction();
    })
    .catch(error => {
        if (error.response && (error.response.status === 401 || error.response.status === 403)) {
                window.location.href = '/';
        } else {
            console.error('ABOBA ERROR', error);
        }
    })
}


export default function HeadPermissions() {
    const api = new ApiDirectory()
    const apiDir = api.getApiUrl()
    const token = getToken();
    const [users, setUsers] = useState();
    const [isLoading, setIsLoading] = useState(false);
    const [username, setUsername] = useState();
    const [email, setEmail] = useState();
    const [password, setPassword] = useState();
    const [confirmedPassword, setConfirmedPassword] = useState();
    const [isChangingPassword, setIsChangingPassword] = useState(false);
    const [userIdToChange, setUserIdToChange] = useState(null);
    const [newPassword, setNewPassword] = useState('');
    const [confirmedNewPassword, setConfirmedNewPassword] = useState('');

    const getUsers = () => {
        setIsLoading(true);
        axios.get(`${apiDir}/head/`, {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
                'ngrok-skip-browser-warning': 'awd',
            }
        })
        .then(response => {
            console.log('пользователи загружены')
            setUsers(response.data);
            setIsLoading(false);
            console.log(response.data);
        })
        .catch(error => {
            if (error.response && (error.response.status === 401 || error.response.status === 403)) {
                    setIsLoading(false);
                    window.location.href = '/';
            } else {
                console.error('ABOBA ERROR', error);
            }
        })
    };


    const deleteThisUser = (id) => {
        axios.delete(`${apiDir}/head/${id}/`,
            {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            getUsers();
        })
        .catch(error => {
            if (error.response && (error.response.status === 401 || error.response.status === 403)) {
                    window.location.href = '/';
            } else {
                console.error('ABOBA ERROR', error);
            }
        })
    }


    const handleChangePassword = (userId) => {
        setUserIdToChange(userId);
        setIsChangingPassword(true);
    };

    const submitChangePassword = () => {
        if (newPassword === confirmedNewPassword) {
            axios.patch(`${apiDir}/head/${userIdToChange}/`, {
                new_password: newPassword,
                confirm_password: confirmedNewPassword,
            }, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                }
            })
            .then(response => {
                console.log('Пароль изменен');
                setIsChangingPassword(false);
                setNewPassword('');
                setConfirmedNewPassword('');
                getUsers(); // Обновляем список пользователей
            })
            .catch(error => {
                console.error('Ошибка при изменении пароля', error);
            });
        } else {
            alert('Пароли не совпадают');
        }
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
                                <strong>Email:</strong> {user.email} <br />
                                <strong>Role:</strong> {user.is_superuser ? 'Руководитель' : 'Работник'}
                                <button type='button' onClick={() => {
                                    const confirmation = window.confirm('Вы уверены, что хотите удалить этого пользователя?');
                                    if (confirmation) {
                                        deleteThisUser(user.id)
                                    }
                                }}>удалить</button>
                                <button type='button' onClick={() => handleChangePassword(user.id)}>изменить пароль</button>
                                {isChangingPassword && user.id === userIdToChange && (
                                    <div>
                                        <input type='password' placeholder='новый пароль' value={newPassword} onChange={e => setNewPassword(e.target.value)} />
                                        <input type='password' placeholder='подтвердите пароль' value={confirmedNewPassword} onChange={e => setConfirmedNewPassword(e.target.value)} />
                                        <button type='button' onClick={submitChangePassword}>Отправить</button>
                                    </div>
                                )}
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
                    getUsers,
                    apiDir);
                }}>добавить</button>
            </div>
            { renderUsers() }
            <Link to='/calculatorFactPlan'>
                <button type='button'>назад</button>
            </Link>
        </>
    )
}
