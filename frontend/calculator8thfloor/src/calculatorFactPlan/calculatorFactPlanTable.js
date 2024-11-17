import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { getToken } from '../tokenService';
import { Link } from 'react-router-dom';
import { ApiDirectory } from '../apiDir';
import '../styles/styles.css';
import Logo from '../img/logo.svg'


export default function CalculatorFactPlanTable(props) {
    const api = new ApiDirectory()
    const apiDir = api.getApiUrl()
    const token = getToken();
    const [factData, setFactData] = useState([]);
    const [planData, setPlanData] = useState([]);
    const [isLoading, setIsLoading] = useState(true);


    const handleDownloadFactExcel = () => {
        axios.get(`${apiDir}/export/fact/excel`, {
            headers: {
                'ngrok-skip-browser-warning': 'skip-browser-warning',
            },
            responseType: 'blob'
        })
            .then(response => {
                console.log(response)
                const url = window.URL.createObjectURL(new Blob([response.data]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', 'fact.xlsx');
                document.body.appendChild(link);
                link.click();
                link.remove();
                window.URL.revokeObjectURL(url);
            })
            .catch(error => {
                console.error('Ошибка при загрузке файла:', error);
            });
    };


    const handleDownloadPlanExcel = () => {
        axios.get(`${apiDir}/export/plan/excel`, {
            headers: {
                'ngrok-skip-browser-warning': 'skip-browser-warning',
            },
            responseType: 'blob'
        })
            .then(response => {
                console.log(response)
                const url = window.URL.createObjectURL(new Blob([response.data]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', 'fact.xlsx');
                document.body.appendChild(link);
                link.click();
                link.remove();
                window.URL.revokeObjectURL(url);
            })
            .catch(error => {
                console.error('Ошибка при загрузке файла:', error);
            });
    };


    const handleDownloadFactPlanExcel = () => {
        axios.get(`${apiDir}/export/fact_plan/excel`, {
            headers: {
                'ngrok-skip-browser-warning': 'skip-browser-warning',
            },
            responseType: 'blob'
        })
            .then(response => {
                console.log(response)
                const url = window.URL.createObjectURL(new Blob([response.data]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', 'fact.xlsx');
                document.body.appendChild(link);
                link.click();
                link.remove();
                window.URL.revokeObjectURL(url);
            })
            .catch(error => {
                console.error('Ошибка при загрузке файла:', error);
            });
    };


    const getFactCalculatedData = () => {
        setIsLoading(true);
        axios.get(`${apiDir}/data/fact/`, {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
                'ngrok-skip-browser-warning': 'awd',
            }
        })
            .then(response => {
                console.log(response)
                setFactData(response.data);
                setIsLoading(false);
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


    const getPlanCalculatedData = () => {
        setIsLoading(true);
        axios.get(`${apiDir}/data/plan/`, {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
                'ngrok-skip-browser-warning': 'awd',
            }
        })
            .then(response => {
                console.log(response)
                setPlanData(response.data);
                setIsLoading(false);
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


    useEffect(() => {
        getFactCalculatedData();
        getPlanCalculatedData();
    }, []);

    const renderFactTable = () => {
        if (isLoading) {
            return (
                <div className="text-center">
                    <div className="spinner-border" role="status">
                        <span className="sr-only">Loading...</span>
                    </div>
                </div>
            );
        }

        if (factData.length === 0) {
            return (
                <tr>
                    <td colSpan="7" className="text-center">Что-то пошло не так, перезагрузите страницу</td>
                </tr>
            );
        }

        return (
            <tbody className='fact-table-body'>
                {factData.map((row, index) => (
                    <tr key={index}>
                        <td>{row.machine_type}</td>
                        <td>{row.month_files}</td>
                        <td>{row.avg_fact_files_per_month}</td>
                        <td>{row.cnt_machines}</td>
                        <td>{row.max_files}</td>
                        <td>{parseInt(row.load_fact * 100)}%</td>
                        <td>{row.scarcity_fact}</td>
                    </tr>
                ))}
            </tbody>
        );
    };


    const renderPlanTable = () => {
        if (isLoading) {
            return (
                <div className="text-center">
                    <div className="spinner-border" role="status">
                        <span className="sr-only">Loading...</span>
                    </div>
                </div>
            );
        }

        if (factData.length === 0) {
            return (
                <tr>
                    <td colSpan="7" className="text-center">Что-то пошло не так, перезагрузите страницу</td>
                </tr>
            );
        }

        return (
            <tbody className='plan-table-body'>
                {planData.map((row, index) => (
                    <tr key={index}>
                        <td>{row.machine_type}</td>
                        <td>{row.cnt_UZ}</td>
                        <td>{row.month_files}</td>
                        <td>{row.avg_fact_files_per_month}</td>
                        <td>{row.avg_fact_files_with_new}</td>
                        <td>{row.cnt_machines}</td>
                        <td>{row.max_files}</td>
                        <td>{parseInt(row.load_plan * 100)}%</td>
                        <td>{row.scarcity_plan}</td>
                    </tr>
                ))}
            </tbody>
        );       
    };


    return (
        <>
            <header>
                <nav className='inputData-navigation'>
                    <img src={Logo} width="50" height="50" style={{ marginRight: "78px" }}></img>
                    <ul>
                        <Link to='/calculatorFactPlan'><button className='calculator-type-button' type='button'>1 калькулятор</button>
                        </Link>
                        <Link to='/pupu1'><button className='calculator-type-button' type='button'>2 калькулятор</button>
                        </Link>
                        <Link to='/pupu2'><button className='calculator-type-button' type='button'>3 калькулятор</button>
                        </Link>
                        <button className='calculator-type-button' type='button' onClick={() => {
                            handleDownloadFactExcel();
                            console.log('нажал');
                        }}>экспорт факта</button>
                        <button className='calculator-type-button' type='button' onClick={() => {
                            handleDownloadPlanExcel();
                            console.log('нажал');
                        }}>экспорт плана</button>
                        <button className='calculator-type-button' type='button' onClick={() => {
                            handleDownloadFactPlanExcel();
                            console.log('нажал');
                        }}>экспорт факта и плана</button>
                    </ul>
                </nav>
            </header>

            <body>
                <div className='body-container'>

                    <div className='table-container'>
                        <div className='vertical-text'>
                            <p>Ф</p>
                            <p>А</p>
                            <p>К</p>
                            <p>Т</p>
                        </div>
                        <table className="table fact-table">
                            <thead className="thead-dark">
                                <tr>
                                    <th></th>
                                    <th>Максимальное количество <br />файлов в месяц</th>
                                    <th>Факт среднего кол-ва <br />файлов в месяц</th>
                                    <th>Факт количества <br />машин</th>
                                    <th>Факт максимального <br />количества файлов</th>
                                    <th>Факт нагрузки в %</th>
                                    <th>Факт нехватки машин</th>
                                </tr>
                            </thead>
                            {renderFactTable()}
                        </table>
                    </div>

                    <div className='table-container'>
                        <div className='vertical-text'>
                            <p>П</p>
                            <p>Л</p>
                            <p>А</p>
                            <p>Н</p>
                        </div>
                        <table className="table plan-table">
                            <thead className="thead-dark">
                                <tr>
                                    <th></th>
                                    <th>Кол-во новых UZ</th>
                                    <th>Мах кол-во <br />файлов в месяц</th>
                                    <th>Факт среднего <br /> кол-ва файлов в месяц</th>
                                    <th>С учетом новых UZ</th>
                                    <th>Факт количества машин</th>
                                    <th>Факт максимального <br /> кол-ва файлов</th>
                                    <th>Планируемая нагрузка в %</th>
                                    <th>Планируемая нехватки машин</th>
                                </tr>
                            </thead>
                            {renderPlanTable()}
                        </table>
                    </div>
                    
                    <div style={{marginLeft: "140px"}}>
                        <Link to='/inputForCalculatorFactPlan'>
                            <button className='calculator-type-button' type='button' style = {{borderColor: "orange"}}>Ввести новые данные</button>
                        </Link>
                        {props.isAdmin && (
                            <Link to='/handleUsersPermisions'>
                                <button className='calculator-type-button' type='button' style = {{borderColor: "orange"}}>доступ пользователей</button>
                            </Link>
                        )}
                    </div>
                </div>
            </body>
        </>
    );
}