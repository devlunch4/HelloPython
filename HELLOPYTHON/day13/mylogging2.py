import logging

simple_formatter = logging.Formatter("[%(name)s] %(message)s")
complex_formatter = logging.Formatter(
    "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(complex_formatter)
console_handler.setLevel(logging.DEBUG)


file_handler = logging.FileHandler("my.log")
file_handler = logging.FileHandler("my.log", mode='a', encoding='utf-8')
file_handler.setFormatter(complex_formatter)
file_handler.setLevel(logging.DEBUG)

root_logger = logging.getLogger()
root_logger.addHandler(console_handler)
root_logger.addHandler(file_handler)
root_logger.setLevel(logging.WARNING)



parent_logger = logging.getLogger("parent")
parent_logger.setLevel(logging.INFO)

child_logger = logging.getLogger("parent.child")
child_logger.setLevel(logging.DEBUG)

