export class ApiDirectory {
    constructor() {
        this.baseUrl = 'http://127.0.0.1:8000/'; // Основной URL вашего бэкенда
    }

    // Метод для получения полного URL для конкретного эндпоинта
    getApiUrl() {
        return `${this.baseUrl}`;
    }
}