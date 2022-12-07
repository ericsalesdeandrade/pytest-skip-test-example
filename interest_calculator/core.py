import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)


def simple_interest(principal: int | float,
                    time_: int | float,
                    rate: int | float) -> int | float:
    logger.debug(f"Principal - {principal}")
    logger.debug(f"Time - {time_}")
    logger.debug(f"Rate - {rate}")

    si = (principal * time_ * rate) / 100
    logger.info(f"The Simple Interest is {si}")
    return si


def compound_interest(principal: int | float,
                      time_: int | float,
                      rate: int | float) -> int | float:
    logger.debug(f"Principal - {principal}")
    logger.debug(f"Time - {time_}")
    logger.debug(f"Rate - {rate}")

    ci = (principal * (1 + rate / 100)) ** time_
    logger.info(f"The Compound Interest is {ci}")
    return ci