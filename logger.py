import logging

def get_logger(name=None):
    root_logger_name = 'combine'

    # Build the name of the sub-logger
    name = f'{root_logger_name}.{name}' if name else root_logger_name
    root_logger = logging.getLogger(root_logger_name)  

    # If the root logger has no handlers, add them
    # in any case return the sub-logger
    if not root_logger.handlers:
        root_logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler() # default to sys.stderr
        ch.setLevel(logging.DEBUG) # todo: make it configurable
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        root_logger.addHandler(ch)
    return logging.getLogger(name)