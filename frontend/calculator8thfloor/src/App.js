import logo from './logo.svg';
import './App.css';
import axios from 'axios';

function App() {
  const fetchHomeData = () => {
    axios.get('http://127.0.0.1:8000/home/')
      .then(response => {
        console.log(response.data);
        // Здесь вы можете обновить состояние или отобразить данные
      })
      .catch(error => {
        console.error('Ошибка:', error);
      });
  };

  const a =() => {
    const inputData = {
      cnt_machines: {
        '180h': 2,
        '168h': 3,
        '79h': 6,
        '180h night': 2
      },
      max_files: {
        '180h day': 6539,
        '168h': 6539,
        '79h': 6539,
        '180h weekend': 1143,
        '180h night': 833,
      },
      cnt_UZ: 600
    };

    axios.post('http://127.0.0.1:8000/data/input/', 
      JSON.stringify(inputData), 
      {
        headers: {
          'Content-Type': 'application/json'
        }
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
        <button onClick={fetchHomeData}>Fetch Home Data</button> {/* Добавьте этот кнопку */}
        <button onClick={a}>update</button> {/* Добавьте этот кнопку */}
      </header>
    </div>
  );
}

export default App;
