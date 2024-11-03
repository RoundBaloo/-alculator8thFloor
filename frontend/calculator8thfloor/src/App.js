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
      </header>
    </div>
  );
}

export default App;
