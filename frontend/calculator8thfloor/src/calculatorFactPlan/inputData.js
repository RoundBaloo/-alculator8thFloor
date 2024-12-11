import React, { useEffect, useState } from 'react'
import axios from 'axios';
import { getToken } from './services/tokenService';
import { Navigate, useSearchParams } from 'react-router-dom';
import { ApiDirectory } from '../apiDir';
import '../styles/styles.css';
import { Link } from 'react-router-dom';
import Logo from '../img/logo.svg';
import icon180h from '../img/h180.svg';
import icon160h from '../img/h160.svg';
import icon79h from '../img/h79.svg';
import day from '../img/day.svg';
import night from '../img/night.svg';
import weekend from '../img/weekend.svg';
import planTableService from './services/planTableService';


const InputData = (props) => {
    const api = new ApiDirectory()
    const apiDir = api.getApiUrl()
    const token = getToken();
    const [cnt180, setCnt180] = useState(0);
    const [cnt168, setCnt168] = useState(0);
    const [cnt79, setCnt79] = useState(0);
    const [files180d, setFiles180d] = useState(0);
    const [files168, setFiles168] = useState(0);
    const [files79, setFiles79] = useState(0);
    const [files180w, setFiles180w] = useState(0);
    const [files180n, setFiles180n] = useState(0);
    const [cntUZ, setCntUZ] = useState(0);
    const [permittedLoad, setPermittedLoad] = useState();
    const [isCalculated, setIsCalculated] = useState(false);
    const [isError, setIsError] = useState(true);

    function getInputData(token) {
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
                    console.error('ABOBA ERROR', error);
                }
            })
    }


    function callUpdateInputData(table) {
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
            'cnt_UZ': cntUZ,
            'permitted_load': permittedLoad,
        }, apiDir, table);
    }


    useEffect(() => {
        console.log('Компонент загружен!');
        getInputData(token);
    }, []);

    const updateInputData = (token, inputData, apiDir, table) => {
        axios.post(`${apiDir}/calculatorFactPlan/data/input/`,
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
                console.log('я вызвался 2 раза')
                console.log(response.data)
                setIsError(false);
            })
            .catch(error => {
                if (error.response && (error.response.status === 401 || error.response.status === 403)) {
                    setIsError(true);
                    window.location.href = '/';
                } else {
                    console.error('ABOBA ERROR', error);
                }
            })
    }

    const handleCalculateButton = (isCalculated, table, isPlanTable) => {
        if (!(isNaN(cnt180) || isNaN(cnt168) || isNaN(cnt79) || isNaN(files180d) 
            || isNaN(files180n) || isNaN(files180w) || isNaN(cntUZ) || isNaN(permittedLoad)
            || cnt180 === 0 || cnt168 === 0 || cnt79 === 0 || files180d === 0 
            || files180n === 0 || files180w === 0 || cntUZ === 0 || permittedLoad == 0)) {
                setIsCalculated(isCalculated);
                callUpdateInputData(table);
                planTableService.setPlanTable(isPlanTable);
            }
    }


    if (isCalculated && !isError) {
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
                        style={isNaN(cnt180) || cnt180 === 0 ? { borderColor: 'red' } : {}} 
                        value={cnt180} 
                        onChange={e => setCnt180(parseInt(e.target.value))}/>
                        <img src={icon180h} className='input-icon'></img>
                    </div>
                    <div className='input-wrapper'>
                        <input type="number"
                        style={isNaN(cnt168) || cnt168 === 0 ? { borderColor: 'red' } : {}}
                         value={cnt168} 
                         onChange={e => setCnt168(parseInt(e.target.value))}/>
                        <img src={icon160h} className='input-icon'></img>
                    </div>
                    <div className='input-wrapper'>
                        <input type="number" 
                        style={isNaN(cnt79) || cnt79 === 0 ? { borderColor: 'red' } : {}}
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
                        style={isNaN(files180d) || files180d === 0 ? { borderColor: 'red' } : {}}
                        value={files180d} onChange={e => {
                            setFiles180d(parseInt(e.target.value));
                            setFiles168(parseInt(e.target.value));
                            setFiles79(parseInt(e.target.value));
                        }}/>
                        <img src={day} className='input-icon'></img>
                    </div>
                    <div className='input-wrapper'>
                        <input type="number" 
                        style={isNaN(files180w) || files180w === 0 ? { borderColor: 'red' } : {}}
                        value={files180w} 
                        onChange={e => setFiles180w(parseInt(e.target.value))}/>
                        <img src={night} className='input-icon'></img>
                    </div>
                    <div className='input-wrapper'>
                        <input type="number" style={isNaN(files180n) || files180n === 0 ? { borderColor: 'red' } : {}}
                        value={files180n} 
                        onChange={e => setFiles180n(parseInt(e.target.value))}/>
                        <img src={weekend} className='input-icon'></img>
                    </div>
                </div>

                <div className='input-container'>
                    <p>Кол-во новых пользователей</p>
                    <input type="number" 
                    style={isNaN(cntUZ) || cntUZ === 0 ? { borderColor: 'red' } : {}}
                    value={cntUZ} 
                    onChange={e => setCntUZ(parseInt(e.target.value))}/>
                </div>

                <div className='input-container'>
                    <p>Разрешенная нагрузка</p>
                    <input type="number" 
                    style={isNaN(permittedLoad) || permittedLoad === 0 ? { borderColor: 'red' } : {}}
                    value={permittedLoad} 
                    onChange={e => setPermittedLoad(parseInt(e.target.value))}/>
                </div>

                <div className='calculate-buttons'>
                    <button type='button'
                            className='calculate-button'
                            onClick={() => {
                                handleCalculateButton(true, 'fact', false);
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
                                handleCalculateButton(true, 'both', true);
                            }}>Рассчитать факт и план
                    </button>
                </div>
            </div>
        </>
    )
}

export default InputData;