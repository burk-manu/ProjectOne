import system
import log

logger = log.setup_logger(name=f"host.{__name__}") # setup logger

def prepare():
    logger.debug("prepare started")

    settings = system.document_reader("settings.config")
    print(settings, type(settings))
    if type(settings) == dict:
        
        max_str_int_conversion = settings.get("max_str_int_conversion", 4300)
        system.set_max_int_len(max_str_int_conversion)
        
        logger.debug(f"max_str_int_conversion set to {max_str_int_conversion}")
