import wolframalpha

import log
import system

logger = log.setup_logger(name=f"host.{__name__}") # setup logger

def wolframalpha_query(calculation): # queries wolframalpha for a calculation
    logger.debug("Querying WolframAlpha")

    api_key = system.document_reader("keys.config", "wolframalpha_short_answer")
    logger.debug(f"API key: {api_key}")
    client = wolframalpha.Client(api_key)
    
    logger.debug(f"Client created with API key: {client.app_id}")

    result = client.query(calculation)
    logger.debug("Query successful")

    return next(result.results).text