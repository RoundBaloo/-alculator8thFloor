import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { getToken } from './services/tokenService';
import { Link } from 'react-router-dom';
import { ApiDirectory } from '../apiDir';
import '../styles/styles.css';
import adminService from './services/adminService';
import planTableService from './services/planTableService';


export default function CalculatorFactPlanTable(props) {
    const api = new ApiDirectory()
    const apiDir = api.getApiUrl()
    const token = getToken();
    const [factData, setFactData] = useState([]);
    const [planData, setPlanData] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const [columnNames, setColumnNames] = useState();


    useEffect(() => {
        getFactCalculatedData();
        getPlanCalculatedData();
        getTableColumnNames();
    }, []);


    const handleDownloadFactExcel = () => {
        axios.get(`${apiDir}/calculatorFactPlan/export/fact/excel`, {
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
        axios.get(`${apiDir}/calculatorFactPlan/export/plan/excel`, {
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
                link.setAttribute('download', 'plan.xlsx');
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
        axios.get(`${apiDir}/calculatorFactPlan/export/fact_plan/excel`, {
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
                link.setAttribute('download', 'fact_and_plan.xlsx');
                document.body.appendChild(link);
                link.click();
                link.remove();
                window.URL.revokeObjectURL(url);
            })
            .catch(error => {
                console.error('Ошибка при загрузке файла:', error);
            });
    };


    const handleDownloadFactPlanWord = () => {
        axios.get(`${apiDir}/calculatorFactPlan/export/report/docx`, {
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
                link.setAttribute('download', 'report.docx');
                document.body.appendChild(link);
                link.click();
                link.remove();
                window.URL.revokeObjectURL(url);
            })
            .catch(error => {
                console.error('Ошибка при загрузке файла:', error);
            });
    };


    const handleDownloadFactPlanPDF = () => {
        axios.get(`${apiDir}/calculatorFactPlan/export/report/pdf`, {
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
                link.setAttribute('download', 'report.pdf');
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
        axios.get(`${apiDir}/calculatorFactPlan/data/fact/`, {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
                'ngrok-skip-browser-warning': 'awd',
            }
        })
            .then(response => {
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
        axios.get(`${apiDir}/calculatorFactPlan/data/plan/`, {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
                'ngrok-skip-browser-warning': 'awd',
            }
        })
            .then(response => {
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


    const getTableColumnNames = () => {
        axios.get(`${apiDir}/calculatorFactPlan/names/`, {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
                'ngrok-skip-browser-warning': 'awd',
            }
        })
        .then(response => {
            console.log(response);
            setColumnNames(response.data[0])
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
                {factData.map((row, index) => {
                    const is180hDay = row.machine_type.startsWith('180h_day');
                    const is168h = row.machine_type === '168h';
                    const is79h = row.machine_type === '79h';
                    const is180hWeekendOrNight = row.machine_type === '180h_weekend' || row.machine_type === '180h_night';
                    const is180hWeekend = row.machine_type === '180h_weekend';
                    const is180hNight = row.machine_type === '180h_night';
                
                    return (
                        <tr key={index}>
                            <td>{row.machine_name}</td>
                            {is180hNight ? (
                                null
                            ) : is180hWeekend ? (
                                <td rowSpan={2}>{row.month_files}</td>
                            ) : (
                                <td>{row.month_files}</td>
                            )}
                            {is180hDay ? (
                                <td rowSpan={3}>{row.avg_fact_files_per_month}</td>
                            ) : (is168h || is79h) ? (
                                // Для 168h и 79h ничего не выводим
                                null
                            ) : is180hWeekendOrNight ? (
                                <td>{row.avg_fact_files_per_month}</td>
                            ) : (
                                <td>&nbsp;</td>
                            )}
                            {is180hNight ? (
                                null
                            ) : is180hWeekend ? (
                                <td rowSpan={2}>{row.cnt_machines}</td>
                            ) : (
                                <td>{row.cnt_machines}</td>
                            )}
                            {is180hNight ? (
                                null
                            ) : is180hWeekend ? (
                                <td rowSpan={2}>{row.max_files}</td>
                            ) : (
                                <td>{row.max_files}</td>
                            )}
                            {is180hDay ? (
                                <td rowSpan={3}>{row.load_fact}%</td>
                            ) : (is168h || is79h) ? (
                                // Для 168h и 79h ничего не выводим
                                null
                            ) : is180hWeekendOrNight ? (
                                <td>{row.load_fact}%</td>
                            ) : (
                                <td>&nbsp;</td>
                            )}  
                            {is180hNight ? (
                                null
                            ) : is180hWeekend ? (
                                <td rowSpan={2}>{row.scarcity_fact}</td>
                            ) : (
                                <td>{row.scarcity_fact}</td>
                            )}
                        </tr>
                    )
                })}
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
                {planData.map((row, index) => {
                    const is180hDay = row.machine_type.startsWith('180h_day');
                    const is168h = row.machine_type === '168h';
                    const is79h = row.machine_type === '79h';
                    const is180hWeekendOrNight = row.machine_type === '180h_weekend' || row.machine_type === '180h_night';
                    const is180hWeekend = row.machine_type === '180h_weekend';
                    const is180hNight = row.machine_type === '180h_night';

                    return (
                        <tr key={index}>
                            <td>{row.machine_name}</td>
                            
                            {is180hNight ? (
                                null
                            ) : is180hWeekend ? (
                                <td rowSpan={2}>{row.month_files}</td>
                            ) : (
                                <td>{row.month_files}</td>
                            )}

                            {is180hDay ? (
                                <td rowSpan={5}>{row.cnt_UZ}</td>
                            ) : (is168h || is79h || is180hWeekendOrNight) ? (
                                null
                            ) : (
                                <td>&nbsp;</td>
                            )}

                            {is180hDay ? (
                                <td rowSpan={3}>{row.avg_fact_files_per_month}</td>
                            ) : (is168h || is79h) ? (
                                // Для 168h и 79h ничего не выводим
                                null
                            ) : is180hWeekendOrNight ? (
                                <td>{row.avg_fact_files_per_month}</td>
                            ) : (
                                <td>&nbsp;</td>
                            )}

                            {is180hDay ? (
                                <td rowSpan={3}>{row.avg_fact_files_with_new}</td>
                            ) : (is168h || is79h) ? (
                                // Для 168h и 79h ничего не выводим
                                null
                            ) : is180hWeekendOrNight ? (
                                <td>{row.avg_fact_files_per_month}</td>
                            ) : (
                                <td>&nbsp;</td>
                            )}

                            {is180hNight ? (
                                null
                            ) : is180hWeekend ? (
                                <td rowSpan={2}>{row.cnt_machines}</td>
                            ) : (
                                <td>{row.cnt_machines}</td>
                            )}

                            {is180hNight ? (
                                null
                            ) : is180hWeekend ? (
                                <td rowSpan={2}>{row.max_files}</td>
                            ) : (
                                <td>{row.max_files}</td>
                            )}

                            {is180hDay ? (
                                <td rowSpan={3}>{row.load_plan}%</td>
                            ) : (is168h || is79h) ? (
                                // Для 168h и 79h ничего не выводим
                                null
                            ) : is180hWeekendOrNight ? (
                                <td>{row.load_plan}%</td>
                            ) : (
                                <td>&nbsp;</td>
                            )}      

                            {is180hNight ? (
                                null
                            ) : is180hWeekend ? (
                                <td rowSpan={2}>{row.scarcity_plan}</td>
                            ) : (
                                <td>{row.scarcity_plan}</td>
                            )}

                        </tr>
                    );
                })}
            </tbody>
        );       
    };

    const [showAllButtons, setShowAllButtons] = useState(false);

    const handleFirstButtonClick = () => {
        console.log('нажал');
        setShowAllButtons(prevState => !prevState);
    };



    return (
        <>
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
                                    <th>{columnNames ? columnNames['month_files'] : "Loading..."}</th>
                                    <th>{columnNames ? columnNames['avg_fact_files_per_month'] : "Loading..."}</th>
                                    <th>{columnNames ? columnNames['cnt_machines'] : "Loading..."}</th>
                                    <th>{columnNames ? columnNames['max_files'] : "Loading..."}</th>
                                    <th>{columnNames ? columnNames['load_fact'] : "Loading..."}</th>
                                    <th>{columnNames ? columnNames['scarcity_fact'] : "Loading..."}</th>
                                </tr>
                            </thead>
                            {renderFactTable()}
                        </table>
                    </div>
                    {planTableService.getPlanTable() ? (
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
                                        <th>{columnNames ? columnNames['month_files'] : "Loading..."}</th>
                                        <th>{columnNames ? columnNames['cnt_UZ'] : "Loading..."}</th>
                                        <th>{columnNames ? columnNames['avg_fact_files_per_month'] : "Loading..."}</th>
                                        <th>{columnNames ? columnNames['avg_fact_files_with_new'] : "Loading..."}</th>
                                        <th>{columnNames ? columnNames['cnt_machines'] : "Loading..."}</th>
                                        <th>{columnNames ? columnNames['max_files'] : "Loading..."}</th>
                                        <th>{columnNames ? columnNames['load_plan'] : "Loading..."}</th>
                                        <th>{columnNames ? columnNames['scarcity_plan'] : "Loading..."}</th>
                                    </tr>
                                </thead>
                                {renderPlanTable()}
                            </table>
                        </div>
                    ) : null}
                    
                    <div style={{marginLeft: "140px"}}>
                        <Link to='/inputForCalculatorFactPlan'>
                            <button className='calculator-type-button' type='button'>Ввести новые данные</button>
                        </Link>
                        <button className={`calculator-type-button-export ${showAllButtons ? 'active' : ''}`}
                                type='button' onClick={handleFirstButtonClick}>Экспорт
                        </button>
                        {showAllButtons && (
                            <>
                                <button className={`calculator-type-button-export type ${showAllButtons ? 'show' : ''}`} type='button' onClick={handleDownloadFactExcel}>
                                    Факт
                                </button>
                                <button className={`calculator-type-button-export type ${showAllButtons ? 'show' : ''}`} type='button' onClick={() => {
                                    handleDownloadPlanExcel();
                                    console.log('нажал');
                                }}>План
                                </button>
                                <button className={`calculator-type-button-export type ${showAllButtons ? 'show' : ''}`} type='button' onClick={() => {
                                    handleDownloadFactPlanExcel();
                                    console.log('нажал');
                                }}>Факт и план
                                </button>
                                <button className={`calculator-type-button-export type ${showAllButtons ? 'show' : ''}`} type='button' onClick={() => {
                                    handleDownloadFactPlanWord();
                                    console.log('нажал');
                                }}>Word
                                </button>
                                <button className={`calculator-type-button-export type last ${showAllButtons ? 'show' : ''}`} type='button' onClick={() => {
                                    handleDownloadFactPlanPDF();
                                    console.log('нажал');
                                }}>Pdf
                                </button>
                            </>
                        )}
                    </div>
                </div>
            </body>
        </>
    );
}