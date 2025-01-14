import requests
from typing import Any, Callable


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def create_user(
        self,
        name: str,
        nickname: str,
        email: str,
        password: str,
        phone_number: str,
        pix_type: str | None = None,
        pix_value: str | None = None,
        image_path: str | None = None,
        on_success: Callable[[Any], None] | None = None,
        on_error: Callable[[str, Exception], None] | None = None,
    ):
        """Handles user registration."""
        url = f"{self.base_url}/users"
        try:
            # Prepare the form data
            form_data = {
                "name": name,
                "nickname": nickname,
                "email": email,
                "password": password,
                "phone_number": phone_number,
            }
            if pix_type:
                form_data["pix_type"] = pix_type
            if pix_value:
                form_data["pix_value"] = pix_value

            files = {}
            image_file = None
            if image_path:
                image_file = open(image_path, "rb")
                files["image"] = ("profile_image.jpg", image_file, "image/jpeg")

            response = requests.post(url, data=form_data, files=files)
            response.raise_for_status()

            if image_file:
                image_file.close()

            data = response.json()
            if on_success:
                on_success(data)

            return data

        except requests.exceptions.HTTPError as http_err:
            error_message = ""
            if response.status_code == 409:
                error_message = "O e-mail já está em uso. Tente outro."
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
