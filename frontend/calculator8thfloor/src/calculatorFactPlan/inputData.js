import React, {useEffect, useState} from 'react'
import axios from 'axios';
import { getToken } from '../tokenService';

const InputData = (props) => {
    const token = getToken();
    const [cnt180, setCnt180] = useState(1);
    const [cnt168, setCnt168] = useState(1);
    const [cnt79, setCnt79] = useState(1);
    const [files180d, setFiles180d] = useState(1);
    const [files168, setFiles168] = useState(1);
    const [files79, setFiles79] = useState(1);
    const [files180w, setFiles180w] = useState(1);
    const [files180n, setFiles180n] = useState(1);
    const [cntUZ, setCntUZ] = useState(1);

    function updateInputData() {
        // const inputData = {
        //     cnt_machines: {
        //         '180h': 2,
        //         '168h': 3,
        //         '79h': 6,
        //     },
        //     avg_fact_files_per_month: {
        //         '180h_day': 6539,
        //         '168h': 6539,
        //         '79h': 6539,
        //         '180h_weekend': 1143,
        //         '180h_night': 833,
        //     },
        //     cnt_UZ: 600
        // };
    
        axios.post('http://127.0.0.1:8000/data/input/', 
            JSON.stringify({
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
                cnt_UZ: cntUZ
            }), 
            {
                headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
                }
            })
            .then(response => {
                console.log(response.data)
            })
            .catch(error => {
                console.error('ABOBA ERROR')
            })
    }

    function getInputData() {
        axios.get('http://127.0.0.1:8000/data/input/', 
          {
            headers: {
              'Authorization': `Bearer ${token}`,
            }
          })
          .then(response => {
            console.log(response.data)
          })
          .catch(error => {
            console.error('ABOBA ERROR')
          })
      }
    
    useEffect(() => {
        console.log('Компонент загружен!');
        getInputData();
    }, []);

    return (
        <>
            <p>Факт наличия машин для времени работы</p>
            <input type="number" value={cnt180} onChange={e => setCnt180(e.target.value)} />
            <input type="number" value={cnt168} onChange={e => setCnt168(e.target.value)} />
            <input type="number" value={cnt79} onChange={e => setCnt79(e.target.value)} />
            <p>Среднее количество файлов на месяц для времени работы</p>
            <input type="number" value={files180d} onChange={e => {
                setFiles180d(e.target.value);
                setFiles168(e.target.value);
                setFiles79(e.target.value);
            }} />
            <input type="number" value={files180w} onChange={e => setFiles180w(e.target.value)} />
            <input type="number" value={files180n} onChange={e => setFiles180n(e.target.value)} />
            <p>Кол-во новых пользователей</p>
            <input type='number' value={cntUZ} onChange={e => setCntUZ(e.target.value)} />
            <button type='button' onClick={updateInputData()}>Рассчитать</button>
        </>
    )
}

export default InputData;