import system
import log

logger = log.setup_logger(name=f"host.{__name__}") # setup logger

def prepare():
    logger.debug("prepare started")

    max_str_int_conversion = system.document_reader("settings.config", "max_str_int_conversion")
    system.set_max_int_len(max_str_int_conversion)
    
    logger.debug(f"max_str_int_conversion set to {max_str_int_conversion}")
