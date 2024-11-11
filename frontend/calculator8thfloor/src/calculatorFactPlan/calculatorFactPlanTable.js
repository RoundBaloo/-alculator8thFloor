import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { getToken } from '../tokenService';
import { Link } from 'react-router-dom';
import { ApiDirectory } from '../apiDir';
import '../styles/styles.css';


export default function CalculatorFactPlanTable(props) {
    const api = new ApiDirectory()
    const apiDir = api.getApiUrl()
    const token = getToken();
    const [data, setData] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const getCalculatedData = () => {
            setIsLoading(true);
            axios.get(`${apiDir}/data/all/`, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json',
                    'ngrok-skip-browser-warning': 'awd',
                }
            })
            .then(response => {
                console.log(response)
                setData(response.data);
                setIsLoading(false);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                setIsLoading(false);
            });
        };

        getCalculatedData();
    }, []);

    const renderTable = () => {
        if (isLoading) {
            return (
                <div className="text-center">
                    <div className="spinner-border" role="status">
                        <span className="sr-only">Loading...</span>
                    </div>
                </div>
            );
        }

        if (data.length === 0) {
            return (
                <tr>
                    <td colSpan="7" className="text-center">Что-то пошло не так, перезагрузите страницу</td>
                </tr>
            );
        }

        return (
            <tbody>
                {data.map((row, index) => (
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

    return (
        <>
            <header>
            <nav>
                <ul>
                <Link to='/calculatorFactPlan'><button type='button'>xxx</button>
                </Link>
                <Link to='/pupu1'>
                </Link>
                <Link to='/pupu2'>
                </Link>
                </ul>
            </nav>
            </header>
            <body>
                <table className="table table-bordered">
                    <thead className="thead-dark">
                        <tr>
                            <th>тип машины</th>
                            <th>Максимальное кол-во файлов в месяц</th>
                            <th>Факт среднего кол-ва файлов в месяц</th>
                            <th>Факт</th>
                            <th>Факт максимального кол-ва файлов</th>
                            <th>Факт нагрузки в %</th>
                            <th>Факт нехватки машин</th>
                        </tr>
                    </thead>
                    {renderTable()}
                </table>
                <Link to='/inputForCalculatorFactPlan'>
                <button type='button'>Ввести новые данные</button>
                </Link> 
                <Link to='/handleUsersPermisions'>
                <button type='button'>доступ пользователей</button>
                </Link> 
            </body>
        </>
    );
}