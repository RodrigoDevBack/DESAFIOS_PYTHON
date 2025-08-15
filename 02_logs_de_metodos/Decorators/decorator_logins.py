from time import time
from datetime import datetime
import logging

#Criando meu logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

#Criando meu handler que irá armazenar em um arquivo .log
handler = logging.FileHandler("02_logs_de_metodos/Decorators/app.log")
handler.setLevel(logging.INFO)

#Criando o formato do log
formatter = logging.Formatter("%(message)s")
handler.setFormatter(formatter)

#Adicono o handler ao logger para linkar os dois
logger.addHandler(handler)


def decorator_log(func: object):
    def wrapper(*args, **kwargs):
        inicio = time()
        result = func(*args, **kwargs)
        fim = time()
        logger.info(log_format(fim, inicio, func))
        return result

    return wrapper


def log_format(fim, inicio, func):
    time_result = f"{(fim - inicio):.4f}"
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    name_func = func.__qualname__.split('.').pop(-1)
    return f"{data_hora} - {name_func} - {time_result}s"