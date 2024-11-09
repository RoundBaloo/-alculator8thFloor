import React from 'react'

export default function calculatorFactPlanTable(props) {
  return (
    <>
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
            <tbody>
                {props.data.length > 0 ? (
                props.data.map((row) => (
                    <tr key={row.id}>
                    <td>{row.machine_type}</td>
                    <td>{row.month_files}</td>
                    <td>{row.avg_fact_files_per_month}</td>
                    <td>{row.cnt_machines}</td>
                    <td>{row.max_files}</td>
                    <td>{row.load}%</td>
                    <td>{row.scarcity}</td>
                    </tr>
                ))
                ) : (
                <tr>
                    <td colSpan="4" className="text-center">Нет доступных продуктов.</td>
                </tr>
                )}
            </tbody>
        </table>
    </>
  )
}
