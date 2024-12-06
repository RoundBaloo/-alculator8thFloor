export class ApiDirectory {
    constructor() {
        this.baseUrl = 'https://6ed4-5-2-55-75.ngrok-free.app'; // Основной URL вашего бэкенда
    }

    // Метод для получения полного URL для конкретного эндпоинта
    getApiUrl() {
        return `${this.baseUrl}`;
    }
}