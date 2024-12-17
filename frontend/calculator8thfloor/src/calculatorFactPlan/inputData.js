import React, { useEffect, useState } from 'react'
import axios from 'axios';
import { getToken } from './services/tokenService';
import { Navigate } from 'react-router-dom';
import { ApiUrl } from '../apiUrl';
import '../styles/styles.css';
import icon180h from '../img/h180.svg';
import icon168h from '../img/h168.svg';
import icon79h from '../img/h79.svg';
import day from '../img/day.svg';
import night from '../img/night.svg';
import weekend from '../img/weekend.svg';
import planTableService from './services/planTableService';


const InputData = (props) => {
    const api = new ApiUrl()
    const apiDir = api.getApiUrl()
    const token = getToken();
    const [cnt180, setCnt180] = useState(0);  // кол-во машин 180часов
    const [cnt168, setCnt168] = useState(0);  // кол-во машин 168 часов
    const [cnt79, setCnt79] = useState(0);  // кол-во машин 79 часов
    const [files180d, setFiles180d] = useState(0);  // кол-во файлов для дневных машин 180ч
    const [files168, setFiles168] = useState(0);  // кол-во файлов для машин 168ч
    const [files79, setFiles79] = useState(0);  // кол-во файлов для машин 79ч
    const [files180w, setFiles180w] = useState(0);  // кол-во файлов для машин 180ч в выходные
    const [files180n, setFiles180n] = useState(0);  // кол-во файлов для ночных машин 180ч
    const [cntUZ, setCntUZ] = useState(0);  // кол-во новых пользователей
    const [permittedLoad, setPermittedLoad] = useState();  // разрешенная нагрузка
    const [isCalculated, setIsCalculated] = useState(false);  // успешно ли произвелись расчеты
    const [isCntUzError, setIsCntUzError] = useState(false);  // состояние для обработки ошибки при вводе кол-ва пользователей

    
    useEffect(() => {
        console.log('Компонент загружен!');
        getInputData(token);
    }, []);


    /**
     * Получает данные для заполнения инпут полей данными с БД
     *
     * @param {str} token - Токен доступа
     */
    const getInputData = (token) => {
        axios.get(`${apiDir}/calculatorFactPlan/data/input/`,
            {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json',
                    'ngrok-skip-browser-warning': 'awd',
                }
            })
            .then(response => {
                console.log(response);
                var data = response.data;
                setCnt180(data[0]['cnt_machines']); 
                setCnt168(data[1]['cnt_machines']);
                setCnt79(data[2]['cnt_machines']);
                setFiles180d(data[0]['avg_fact_files_per_month']);
                setFiles168(data[0]['avg_fact_files_per_month']);
                setFiles79(data[0]['avg_fact_files_per_month']);
                setFiles180w(data[3]['avg_fact_files_per_month']);
                setFiles180n(data[4]['avg_fact_files_per_month']);
                setCntUZ(data[0]['cnt_UZ']);
                setPermittedLoad(data[0]['permitted_load']);
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
     * Заполняет массив данными, необходимыми для отправления запроса на обновление записей в БД
     *
     * @param {str} table - Таблица, которую нужно обновить: fact - Факт, plan - План, both - обе
     */
    const callUpdateInputData = (table) => {
        updateInputData(token, {
            cnt_machines: {
                '180h': cnt180,
                '168h': cnt168,
                '79h': cnt79,
            },
            avg_fact_files_per_month: {
                '180h_day': files180d,
                '168h': files168,
                '79h': files79,
                '180h_weekend': files180w,
                '180h_night': files180n,
            },
            'cnt_UZ': isNaN(cntUZ) ? 0 : cntUZ,
            'permitted_load': permittedLoad,
        }, apiDir, table);
    }

    
    /**
     * Отправляет запрос для обновление записей в БД
     *
     * @param {str} token - Токен доступа
     * @param {dict} inputData - Значения, необходимые для расчетов
     * @param {str} apiUrl - URL адрес API
     * @param {str} table - Таблица, которую нужно обновить: fact - Факт, plan - План, both - обе
     */
    const updateInputData = (token, inputData, apiUrl, table) => {
        axios.post(`${apiUrl}/calculatorFactPlan/data/input/`,
            null,
            {
                params: {
                    'data': JSON.stringify(inputData),
                    'table': table,
                },
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                }
            })
            .then(response => {
                setIsCalculated(true);
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
     * Обработчик нажатия кнопки "Рассчитать факт"
     *
     * @param {str} table - Таблица, которую нужно обновить: fact - Факт, plan - План, both - обе
     * @param {bool} isPlanTable - Считаем ли таблицу План
     */
    const handleFactCalculateButton = (table, isPlanTable) => {
        if (!(isNaN(cnt180) || isNaN(cnt168) || isNaN(cnt79) || isNaN(files180d) 
            || isNaN(files180n) || isNaN(files180w) || isNaN(permittedLoad)
            || files180d <= 0 || cnt180 <= 0 || cnt168 < 0 || cnt79 < 0 
            || files180n <= 0 || files180w <= 0 || permittedLoad <= 0)) {
                callUpdateInputData(table);
                planTableService.setPlanTable(isPlanTable);
            }
    }


    /**
     * Обработчик нажатия кнопки "Рассчитать факт и план"
     *
     * @param {str} table - Таблица, которую нужно обновить: fact - Факт, plan - План, both - обе
     * @param {bool} isPlanTable - Считаем ли таблицу План
     */
    const handleFactPlanCalculateButton = (table, isPlanTable) => {
        if (isNaN(cntUZ)) {
            setIsCntUzError(true);
        } else {
            if (!(isNaN(cnt180) || isNaN(cnt168) || isNaN(cnt79) || isNaN(files180d) 
                || isNaN(files180n) || isNaN(files180w) || isNaN(cntUZ) || isNaN(permittedLoad)
                || files180d <= 0 || cnt180 <= 0 || cnt168 < 0 || cnt79 < 0 
                || files180n <= 0 || files180w <= 0 || cntUZ <= 0 || permittedLoad <= 0)) {
                    callUpdateInputData(table);
                    planTableService.setPlanTable(isPlanTable);
                }
        }
    }    


    if (isCalculated) {
        return <Navigate to='/calculatorFactPlan' />
    }


    return (
        <>
            <div className='input-data-main-form'>
                <h1>Факт и план</h1>

                <div className='input-container'>
                    <p>Факт наличия машин для времени работы</p>
                    <div className='input-wrapper'>
                        <input type="number" 
                        style={isNaN(cnt180) || cnt180 <= 0 ? { borderColor: 'red' } : {}} 
                        value={cnt180} 
                        onChange={e => setCnt180(parseInt(e.target.value))}/>
                        <img src={icon180h} className='input-icon'></img>
                    </div>
                    <div className='input-wrapper'>
                        <input type="number"
                        style={isNaN(cnt168) ? { borderColor: 'red' } : {}}
                         value={cnt168} 
                         onChange={e => setCnt168(parseInt(e.target.value))}/>
                        <img src={icon168h} className='input-icon'></img>
                    </div>
                    <div className='input-wrapper'>
                        <input type="number" 
                        style={isNaN(cnt79) ? { borderColor: 'red' } : {}}
                        value={cnt79} 
                        onChange={e => setCnt79(parseInt(e.target.value))}/>
                        <img src={icon79h} className='input-icon min-fact'></img>
                    </div>
                </div>

                <div className='input-container'>
                    <p>Среднее количество файлов на месяц для времени работы</p>
                    <div className='input-wrapper'>
                        <input 
                        type="number" 
                        style={isNaN(files180d) || files180d <= 0 ? { borderColor: 'red' } : {}}
                        value={files180d} onChange={e => {
                            setFiles180d(parseInt(e.target.value));
                            setFiles168(parseInt(e.target.value));
                            setFiles79(parseInt(e.target.value));
                        }}/>
                        <img src={day} className='input-icon'></img>
                    </div>
                    <div className='input-wrapper'>
                        <input type="number" 
                        style={isNaN(files180w) || files180w <= 0 ? { borderColor: 'red' } : {}}
                        value={files180w} 
                        onChange={e => setFiles180w(parseInt(e.target.value))}/>
                        <img src={night} className='input-icon'></img>
                    </div>
                    <div className='input-wrapper'>
                        <input type="number" style={isNaN(files180n) || files180n <= 0 ? { borderColor: 'red' } : {}}
                        value={files180n} 
                        onChange={e => setFiles180n(parseInt(e.target.value))}/>
                        <img src={weekend} className='input-icon'></img>
                    </div>
                </div>

                <div className='input-container'>
                    <p>Кол-во новых пользователей</p>
                    <input type="number" 
                    style={isCntUzError ? { borderColor: 'red' } : {}}
                    value={cntUZ} 
                    onChange={e => {
                        setCntUZ(parseInt(e.target.value));
                        setIsCntUzError(false);
                        }}/>
                </div>

                <div className='input-container'>
                    <p>Разрешенная нагрузка</p>
                    <input type="number" 
                    style={isNaN(permittedLoad) || permittedLoad <= 0 ? { borderColor: 'red' } : {}}
                    value={permittedLoad} 
                    onChange={e => setPermittedLoad(parseInt(e.target.value))}/>
                </div>

                <div className='calculate-buttons'>
                    <button type='button'
                            className='calculate-button'
                            onClick={() => {
                                handleFactCalculateButton('fact', false);
                            }}>Рассчитать факт
                    </button>
                    {/* <button type='button'
                    className='calculate-button' 
                    onClick={() => {
                        setIsCalculated(true);
                        callUpdateInputData('plan');
                    }}>Рассчитать план</button> */}
                    <button type='button'
                            className='calculate-button second'
                            onClick={() => {
                                handleFactPlanCalculateButton('both', true);
                            }}>Рассчитать факт и план
                    </button>
                </div>
            </div>
        </>
    )
}

export default InputData;