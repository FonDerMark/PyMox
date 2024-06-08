import requests


class Request:
    def __init__(self, url, method='GET', params=None, data=None, headers=None, timeout=10):
        """
        Инициализация класса Request.

        :param url: URL для запроса.
        :param method: HTTP метод (GET, POST, PUT, DELETE, HEAD, и т.д.).
        :param params: Параметры URL.
        :param data: Данные для тела запроса.
        :param headers: Заголовки HTTP.
        :param timeout: Таймаут для запроса в секундах.
        """
        self.url = url
        self.method = method.upper()
        self.params = params
        self.data = data
        self.headers = headers
        self.timeout = timeout

    def get_url(self):
        return self.url

    def request(self):
        """
        Выполняет HTTP запрос и возвращает ответ.

        :return: Ответ от сервера.
        """
        try:
            response = requests.request(
                method=self.method,
                url=self.url,
                params=self.params,
                data=self.data,
                headers=self.headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
