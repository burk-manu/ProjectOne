import wolframalpha

import log
import system

logger = log.setup_logger(name=f"host.{__name__}") # setup logger

def wolframalpha_query(calculation): # queries wolframalpha for a calculation
    logger.debug("Querying WolframAlpha")

    env = system.document_reader(r".env", dir="")
    if env == None:
        logger.error("Environment file not found")
        return "Environment file not found"
    elif type(env) == dict:
        api_key = env.get("wolframalpha")
        logger.debug(f"API key: {api_key}")
        client = wolframalpha.Client(api_key)
        
        logger.debug(f"Client created with API key: {client.app_id}")

        result = client.query(calculation)
        logger.debug("Query successful")

        return next(result.results).text
    else:
        logger.error("Environment file not in correct format")
        return "Environment file not in correct format"