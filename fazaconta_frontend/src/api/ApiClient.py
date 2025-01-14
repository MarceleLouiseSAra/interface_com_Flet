import requests
from typing import Any, Callable


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def login(
        self,
        email: str,
        password: str,
        on_success: Callable[[Any], None] | None = None,
        on_error: Callable[[str, Exception], None] | None = None,
    ):
        """Handles user login."""
        url = f"{self.base_url}/sessions/login"
        payload = {"email": email, "password": password}
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            if on_success:
                on_success(data)
            return data
        except requests.exceptions.HTTPError as http_err:
            error_message = ""
            if response.status_code == 401:
                error_message = "Credenciais inválidas. Tente novamente."
            elif response.status_code == 403:
                error_message = "Acesso proibido."
            else:
                error_message = f"Erro: {response.json()}"

            if on_error:
                on_error(error_message, http_err)

            print(error_message)
        except Exception as err:
            error_message = f"Erro: {str(err)}"
            if on_error:
                on_error(error_message, err)

            print(error_message)

    def logout(
        self,
        token: str,
        on_success: Callable[[Any], None] | None = None,
        on_error: Callable[[str, Exception], None] | None = None,
    ):
        """Handles user logout."""
        url = f"{self.base_url}/sessions/logout"
        headers = {"Authorization": f"Bearer {token}"}
        try:
            response = requests.post(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            if on_success:
                on_success(data)
            return data
        except requests.exceptions.HTTPError as http_err:
            error_message = ""
            if response.status_code == 404:
                error_message = "Usuário não encontrado."
            else:
                error_message = f"Erro: {response.status_code}"

            if on_error:
                on_error(error_message, http_err)

            print(error_message)

        except Exception as err:
            error_message = f"Erro: {err}"
            if on_error:
                on_error(error_message, err)

            print(error_message)


api_client = ApiClient("http://localhost:8000")
