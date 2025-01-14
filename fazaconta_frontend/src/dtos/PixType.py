from enum import Enum


class PixType(str, Enum):
    EMAIL = "email"
    CPF_CNPJ = "cpf_cnpj"
    PHONE_NUMBER = "phone_number"
    RANDOM = "random"
