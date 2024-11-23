import wolframalpha

import log

logger = log.setup_logger(name=f"host.{__name__}") # setup logger

def wolframalpha_query(calculation): # queries wolframalpha for a calculation
    logger.debug("Querying WolframAlpha")
    client = wolframalpha.Client("5VYEA9-PT7KE82TX7")
    logger.debug(f"Client created with API key: {client.app_id}")

    result = client.query(calculation)
    logger.debug("Query successful")

    return next(result.results).text
