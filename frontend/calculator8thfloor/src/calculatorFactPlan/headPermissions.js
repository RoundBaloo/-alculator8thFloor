import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { getToken } from '../calculatorFactPlan/services/tokenService';
import { ApiUrl } from '../apiUrl';
import '../styles/styles.css';
import DeleteMember from '../img/delete_member_icon.svg';
import ChangeMember from '../img/change_member_icon.svg';
import { switchButtons } from './stepaScripts/switchButtons';
import { showAddUserForm } from './stepaScripts/showAddUserForm';
import WhitePlusIcon from '../img/white_plus_icon.svg';
import OrangePlusIcon from '../img/orange-plus-icon.svg';
import { hideAddUserButton } from './stepaScripts/hideAddUserButton';
import { showAddUserButton } from './stepaScripts/showAddUserButton';
import { hideRegisterForm } from './stepaScripts/hideRegisterForm';


export default function HeadPermissions(props) {
    const api = new ApiUrl()
    const apiUrl = api.getApiUrl()
    const token = getToken();
    const [users, setUsers] = useState();  // список пользователей
    const [username, setUsername] = useState('');  // логин при добавлении пользователя
    const [email, setEmail] = useState('');  // почта при добавлении пользователя
    const [password, setPassword] = useState('');  // пароль при добавлении пользователя
    const [confirmedPassword, setConfirmedPassword] = useState('');  // подтвержденеи пароля при добавлении пользователя
    const [isChangingPassword, setIsChangingPassword] = useState(false);  // нужно ли отображать форму изменения пароля
    const [userIdToChange, setUserIdToChange] = useState(null);  // ID юзера, которому меняют пароль
    const [newPassword, setNewPassword] = useState('');  // пароль при изменении пароля
    const [confirmedNewPassword, setConfirmedNewPassword] = useState('');  // подтверждение пароля при изменении пароля
    const [currentUser, setCurrentUser] = useState();  // текущий пользователь
    const [isUsernameFilled, setIsUsernameFilled] = useState(true);  // заполнено ли поле логина при добавлении пользователя
    const [isPasswordFilled, setIsPasswordFilled] = useState(true);  // заполнено ли поле пароля при добавлении пользователя
    const [isConfirmedPasswordFilled, setIsConfirmedPasswordFilled] = useState(true);  // заполнено ли поле подтверждения пароля при добавлении пользователя
    const [isEmailFilled, setIsEmailFilled] = useState(true);  // заполнено ли поле эмейла при добавлении пользователя
    const [isNewPasswordFilled, setIsNewPasswordFilled] = useState(true);  // заполнено ли поле пароля при изменении
    const [isConfirmedNewPasswordFilled, setIsConfirmedNewPasswordFilled] = useState(true);  // заполнено ли поле подтверждения при изменении


    useEffect(() => {
        getUsers();
    }, []);


    /** Получает список пользователей */
    const getUsers = () => {
        axios.get(`${apiUrl}/calculatorFactPlan/head/`, {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
                'ngrok-skip-browser-warning': 'awd',
            }
        })
            .then(response => {
                console.log('пользователи загружены')
                setUsers(response.data);
                console.log(response.data);
            })
            .catch(error => {
                if (error.response && (error.response.status === 401 || error.response.status === 403)) {
                    window.location.href = '/';
                } else {
                    console.error(error);
                }
            })
    };


    
    /**
     * Создает пользователя
     *
     * @param {str} token - Токен доступа
     * @param {dict} createUserData - Данные для создания пользователя: логин, пароль и эмейл
     * @param {func} getUsersFunction - Функция для обновления списка пользователей
     */
    const createUser = (token, createUserData, getUsersFunction) => {
        axios.post(`${apiUrl}/calculatorFactPlan/head/`,
            JSON.stringify({
                "username": `${createUserData.username}`,
                "email": `${createUserData.email}`,
                "password": `${createUserData.password}`,
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
                    console.error(error);
                }
            })
    }

    
    /**
     * Удалаяет определенного пользователя
     *
     * @param {int} id - ID пользователя, которого нужно удалить
     */
    const deleteThisUser = (id) => {
        axios.delete(`${apiUrl}/calculatorFactPlan/head/${id}/`,
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
                    console.error(error);
                }
            })
    }


    
    /**
     * Обрабатывает форму изменения пароля, включает отображение формы полей ввода для смены пароля
     *
     * @param {int} userId - ID пользователя, у которого нужно поменять пароль
     */
    const handleChangePassword = (userId) => {
        setUserIdToChange(userId);
        setIsChangingPassword(true);
    };


    
    /** Отправка измененного пароля на сервер */
    const submitChangePassword = () => {
        if (newPassword === confirmedNewPassword) {
            axios.patch(`${apiUrl}/calculatorFactPlan/head/${userIdToChange}/`, {
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
                    getUsers(); 
                })
                .catch(error => {
                    console.error('Ошибка при изменении пароля', error);
                });
        } else {
            alert('Пароли не совпадают');
        }
    };


    
    /**
     * Отрисовывает список пользователь
     *
     * @returns {*} - список пользователей
     */
    const renderUsers = () => {
        if (users) {
            return (
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
                                <input 
                                    type='text' 
                                    value={username} 
                                    onChange={e => (setUsername(e.target.value))} 
                                    style={{borderColor: !isUsernameFilled && 'red'}} />
                                <small>Логин</small>
                            </div>
                            <div className='password-container'>
                                <div className='input-inner'>
                                    <input 
                                        type='password' 
                                        value={password} 
                                        onChange={e => (setPassword(e.target.value))} 
                                        style={{
                                        borderColor: !isPasswordFilled && 'red'}} />
                                    <small>Пароль</small>
                                </div>
                                <div className='input-inner'>
                                    <input 
                                        type='password' 
                                        value={confirmedPassword} 
                                        onChange={e => (setConfirmedPassword(e.target.value))} 
                                        style={{borderColor: !isConfirmedPasswordFilled && 'red'}} />
                                    <small>Подтвердите пароль</small>
                                </div>
                            </div>
                            <div className='input-inner'>
                                <input 
                                    type='email' 
                                    value={email} 
                                    onChange={e => (setEmail(e.target.value))} 
                                    style={{borderColor: !isEmailFilled && 'red'}} />
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
                                        apiUrl);
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
                                <div className='password-container'>
                                    <input 
                                        type='password' 
                                        placeholder='новый пароль' 
                                        value={newPassword} 
                                        onChange={e => {
                                            setNewPassword(e.target.value);
                                            setIsNewPasswordFilled(true);
                                        }}
                                        style={{borderColor: !isNewPasswordFilled && 'red'}} />
                                    <input 
                                        type='password' 
                                        placeholder='подтвердите пароль' 
                                        value={confirmedNewPassword} 
                                        onChange={e => {
                                            setConfirmedNewPassword(e.target.value);
                                            setIsConfirmedNewPasswordFilled(true);
                                        }}
                                        style={{borderColor: !isConfirmedNewPasswordFilled && 'red'}} />
                                </div>
                                <button className='send-changed-password' type='button' onClick={() => {
                                    if (newPassword.length === 0) {
                                        setIsNewPasswordFilled(false);
                                    } else if (confirmedNewPassword.length === 0) {
                                        setIsConfirmedNewPasswordFilled(false);
                                    } else {
                                        setIsNewPasswordFilled(true);
                                        setIsConfirmedNewPasswordFilled(true);

                                        submitChangePassword();
                                    }
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
            {renderUsers()}
        </>
    )
}
