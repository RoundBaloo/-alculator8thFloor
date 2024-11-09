import logo from './logo.svg';
import './App.css';
import axios from 'axios';

var access;

function App1() {
  const a =() => {
    const inputData = {
      cnt_machines: {
        '180h': 2,
        '168h': 3,
        '79h': 6,
      },
      avg_fact_files_per_month: {
        '180h_day': 6539,
        '168h': 6539,
        '79h': 6539,
        '180h_weekend': 1143,
        '180h_night': 833,
      },
      cnt_UZ: 600
    };

    axios.post('http://127.0.0.1:8000/data/input/', 
      JSON.stringify(inputData), 
      {
        headers: {
          'Authorization': `Bearer ${access}`,
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

  const b =() => {
    const inputData = {
      "username": "a@a.com",
      "password": "12345",
    };

    axios.post('http://127.0.0.1:8000/api/token/', 
      JSON.stringify(inputData), 
      {
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => {
        access = response.data.access
        console.log(access)
      })
      .catch(error => {
        console.error('ABOBA ERROR')
      })
  }

  const c =() => {
    axios.get('http://127.0.0.1:8000/data/all/', 
      {
        headers: {
          'Authorization': `Bearer ${access}`,
        }
      })
      .then(response => {
        console.log(response.data)
      })
      .catch(error => {
        console.error('ABOBA ERROR')
      })
  }

  const d =() => {
    axios.get('http://127.0.0.1:8000/head/', 
      {
        headers: {
          'Authorization': `Bearer ${access}`,
        }
      })
      .then(response => {
        console.log(response.data)
      })
      .catch(error => {
        console.error('ABOBA ERROR')
      })
  }

  const e =() => {
    var newUserData = {
      'email': 'a@a.com',
      'password': '12345',
    }

    axios.post('http://127.0.0.1:8000/head/', 
      newUserData,
      {
        headers: {
          'Authorization': `Bearer ${access}`,
        }
      })
      .then(response => {
        console.log(response.data)
      })
      .catch(error => {
        console.error('ABOBA ERROR')
      })
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <button onClick={a}>update</button> {/* Добавьте этот кнопку */}
        <button onClick={b}>auth</button> {/* Добавьте этот кнопку */}
        <button onClick={c}>data</button> {/* Добавьте этот кнопку */}
        <button onClick={d}>head</button> {/* Добавьте этот кнопку */}
        <button onClick={e}>reg</button> {/* Добавьте этот кнопку */}
      </header>
    </div>
  );
}

export default App1;
