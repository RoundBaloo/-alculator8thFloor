import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { getToken } from '../calculatorFactPlan/services/tokenService';
import { Link } from 'react-router-dom';
import { ApiDirectory } from '../apiDir';
import '../styles/styles.css';
import Logo from '../img/logo.svg';
import DeleteMember from '../img/delete_member_icon.svg';
import ChangeMember from '../img/change_member_icon.svg';
import { switchButtons } from './stepaScripts/switchButtons';
import { showAddUserForm } from './stepaScripts/showAddUserForm';
import WhitePlusIcon from '../img/white_plus_icon.svg';
import OrangePlusIcon from '../img/orange-plus-icon.svg';
import { hideAddUserButton } from './stepaScripts/hideAddUserButton';
import { showAddUserButton } from './stepaScripts/showAddUserButton';
import { hideRegisterForm } from './stepaScripts/hideRegisterForm';



const createUser = (token, createUserInformatiom, getUsersFunction, apiDir) => {
    axios.post(`${apiDir}/calculatorFactPlan/head/`,
        JSON.stringify({
            "username": `${createUserInformatiom.username}`,
            "email": `${createUserInformatiom.email}`,
            "password": `${createUserInformatiom.password}`,
        }), {
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


export default function HeadPermissions(props) {
    const api = new ApiDirectory()
    const apiDir = api.getApiUrl()
    const token = getToken();
    const [users, setUsers] = useState();
    const [isLoading, setIsLoading] = useState(false);
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmedPassword, setConfirmedPassword] = useState('');
    const [isChangingPassword, setIsChangingPassword] = useState(false);
    const [userIdToChange, setUserIdToChange] = useState(null);
    const [newPassword, setNewPassword] = useState('');
    const [confirmedNewPassword, setConfirmedNewPassword] = useState('');
    const [currentUser, setCurrentUser] = useState();
    const [isUsernameFilled, setIsUsernameFilled] = useState(true);
    const [isPasswordFilled, setIsPasswordFilled] = useState(true);
    const [isConfirmedPasswordFilled, setIsConfirmedPasswordFilled] = useState(true);
    const [isEmailFilled, setIsEmailFilled] = useState(true);

    const getUsers = () => {
        setIsLoading(true);
        axios.get(`${apiDir}/calculatorFactPlan/head/`, {
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
        axios.delete(`${apiDir}/calculatorFactPlan/head/${id}/`,
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
            axios.patch(`${apiDir}/calculatorFactPlan/head/${userIdToChange}/`, {
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
                    showAddUserButton();
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
                // <div className="users">
                //     <h3>Users:</h3>
                //     <ul>
                //         {users.map((user) => (
                //             <li key={user.id} className='users-item'>
                //                 <strong>Username:</strong> {user.username} <br />
                //                 <strong>Email:</strong> {user.email} <br />
                //                 <strong>Role:</strong> {user.is_superuser ? 'Руководитель' : 'Работник'}
                //                 <button className='delete-button' type='button' onClick={() => {
                //                     const confirmation = window.confirm('Вы уверены, что хотите удалить этого пользователя?');
                //                     if (confirmation) {
                //                         deleteThisUser(user.id)
                //                     }
                //                 }}>удалить</button>
                //                 <button className='change-button' type='button' onClick={() => handleChangePassword(user.id)}>изменить пароль</button>
                //                 {isChangingPassword && user.id === userIdToChange && (
                //                     <div>
                //                         <input type='password' placeholder='новый пароль' value={newPassword} onChange={e => setNewPassword(e.target.value)} />
                //                         <input type='password' placeholder='подтвердите пароль' value={confirmedNewPassword} onChange={e => setConfirmedNewPassword(e.target.value)} />
                //                         <button type='button' onClick={submitChangePassword}>Отправить</button>
                //                     </div>
                //                 )}
                //             </li>
                //         ))}
                //     </ul>
                // </div>
                <>
                    <div className='table-wrapper'>
                        <table className='users'>
                            <thead>
                                <tr>
                                    <th>Логин</th>
                                    <th>Почта</th>
                                    <th>Роль</th>
                                </tr>
                            </thead>
                            <tbody>
                                {users.map((user) => (
                                    <tr key={user.id} className='info-row' onMouseEnter={switchButtons}>
                                        <td>{user.username}</td>
                                        <td>{user.email}</td>
                                        <td>{user.is_superuser ? 'Руководитель' : 'Работник'}</td>
                                        <td className='edit-buttons'>
                                            <button
                                                className='change-button'
                                                type='button'
                                                onClick={() => {
                                                    handleChangePassword(user.id);
                                                    setCurrentUser(user);
                                                    hideAddUserButton();
                                                }}><img src={ChangeMember}></img></button>
                                            {/* {isChangingPassword && user.id === userIdToChange && (
                                                <div>
                                                    <input type='password' placeholder='новый пароль' value={newPassword} onChange={e => setNewPassword(e.target.value)} />
                                                    <input type='password' placeholder='подтвердите пароль' value={confirmedNewPassword} onChange={e => setConfirmedNewPassword(e.target.value)} />
                                                    <button type='button' onClick={submitChangePassword}>Отправить</button>
                                                </div>
                                            )} */}
                                            <button
                                                className='delete-button'
                                                type='button'
                                                onClick={() => {
                                                    if (!user.is_superuser){
                                                        const confirmation = window.confirm('Вы уверены, что хотите удалить этого пользователя?');
                                                        if (confirmation) {
                                                            deleteThisUser(user.id)
                                                        }
                                                    } else {
                                                        alert('Невозможно удалить руководителя')
                                                    }
                                                }}><img src={DeleteMember}></img></button>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                        <button className='add-user' onClick={showAddUserForm}><img src={WhitePlusIcon} style={{ marginRight: "20px" }}></img>Добавить пользователя</button>

                        <div className="register">
                            <div className='input-inner'>
                                <input type='text' value={username} onChange={e => (setUsername(e.target.value))} style={{
                                    borderColor: !isUsernameFilled && 'red',
                                }} />
                                <small>Логин</small>
                            </div>
                            <div className='password-container'>
                                <div className='input-inner'>
                                    <input type='password' value={password} onChange={e => (setPassword(e.target.value))} style={{
                                    borderColor: !isPasswordFilled && 'red',
                                }} />
                                    <small>Пароль</small>
                                </div>
                                <div className='input-inner'>
                                    <input type='password' value={confirmedPassword} onChange={e => (setConfirmedPassword(e.target.value))} style={{
                                    borderColor: !isConfirmedPasswordFilled && 'red',
                                }} />
                                    <small>Подтвердите пароль</small>
                                </div>
                            </div>
                            <div className='input-inner'>
                                <input type='email' value={email} onChange={e => (setEmail(e.target.value))} style={{
                                    borderColor: !isEmailFilled && 'red',
                                }} />
                                <small>Почта</small>
                            </div>
                            <button type='button' className='confirm-add-user' onClick={() => {
                                if (username.length === 0) {
                                    setIsUsernameFilled(false);
                                } else if (password.length === 0) {
                                    setIsUsernameFilled(true);
                                    setIsPasswordFilled(false);
                                } else if (confirmedPassword.length === 0) {
                                    setIsPasswordFilled(true);
                                    setIsConfirmedPasswordFilled(false);
                                } else if (email.length === 0) {
                                    setIsConfirmedPasswordFilled(true);
                                    setIsEmailFilled(false);
                                } else {
                                    setIsUsernameFilled(true);
                                    setIsPasswordFilled(true);
                                    setIsConfirmedPasswordFilled(true);
                                    setIsEmailFilled(true);
                                    createUser(token, {
                                        "username": username,
                                        "email": email,
                                        "password": password,
                                    },
                                        getUsers,
                                        apiDir);
                                    hideRegisterForm();
                                    showAddUserButton();
                                    setUsername('');
                                    setPassword('');
                                    setConfirmedPassword('');
                                    setEmail('');
                                }
                            }}>
                                <img src={OrangePlusIcon} style={{ marginRight: "15px", paddingTop: "3px" }} /> Добавить
                            </button>
                            <button type='button' className='confirm-add-user' onClick={() => {
                                hideRegisterForm();
                                showAddUserButton();
                            }}>
                                Отменить
                            </button>
                        </div>

                        {isChangingPassword && currentUser.id === userIdToChange && (
                            <div className='change-password-container'>
                                <div className='input-inner'>
                                    <input type='text' onChange={e => (setUsername(e.target.value))} />
                                    <small>Логин</small>
                                </div>

                                <div className='password-container'>
                                    <input type='password' placeholder='новый пароль' value={newPassword} onChange={e => setNewPassword(e.target.value)} />
                                    <input type='password' placeholder='подтвердите пароль' value={confirmedNewPassword} onChange={e => setConfirmedNewPassword(e.target.value)} />
                                </div>

                                <div className='input-inner'>
                                    <input type='email' onChange={e => (setEmail(e.target.value))} />
                                    <small>Почта</small>
                                </div>
                                <button className='send-changed-password' type='button' onClick={() => {
                                    submitChangePassword();
                                }}>Отправить</button>
                                <button type='button' className='confirm-add-user' onClick={() => {
                                    setIsChangingPassword(false);
                                    showAddUserButton();
                                }}>
                                    Отменить
                                </button>
                            </div>
                        )}


                    </div>
                </>
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
            {/* <div className="register">
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
            </div> */}
            {renderUsers()}
            {/* <Link to='/calculatorFactPlan'>
                <button className='calculator-type-button return-back' type='button'>назад</button>
            </Link> */}
        </>
    )
}
