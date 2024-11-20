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
        axios.get(`${apiDir}/calculatorFactPlan/data/plan/`, {
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
                {factData.map((row, index) => {
                    console.log(row.machine_name)
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
            <header>
                <nav className='inputData-navigation'>
                    <img src={Logo} width="50" height="50" style={{ marginRight: "78px" }}></img>
                    <ul className={'headerButtons'}>
                        <Link to='/calculatorFactPlan'>
                            <button
                                className={`calculator-type-button ${props.currentCalculator !== 'calculatorFactPlan' ? 'nav-calculator-type-button' : ''}`}
                                type='button'>1 калькулятор
                            </button>
                        </Link>
                        <Link to='/pupu1'>
                            <button
                                className={`calculator-type-button ${props.currentCalculator !== 'calculator1' ? 'nav-calculator-type-button' : ''}`}
                                type='button'>2 калькулятор
                            </button>
                        </Link>
                        <Link to='/pupu2'>
                            <button
                                className={`calculator-type-button ${props.currentCalculator !== 'calculator2' ? 'nav-calculator-type-button' : ''}`}
                                type='button'>3 калькулятор
                            </button>
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
                                    <th>Мах кол-во <br />файлов в месяц</th>
                                    <th>Кол-во новых UZ</th>
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
                            <button className='calculator-type-button' type='button'>Ввести новые данные</button>
                        </Link>
                        {props.isAdmin && (
                            <Link to='/handleUsersPermisions'>
                                <button className='calculator-type-button' type='button'>Управление доступом</button>
                            </Link>
                        )}
                    </div>
                </div>
            </body>
        </>
    );
}