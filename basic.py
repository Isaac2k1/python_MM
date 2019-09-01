import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - [%(levelname)s] [%(threadName)s] (%(module)s:%(lineno)d) %(message)s", )

logging.debug('Some additional information')
logging.info('Working...')
logging.warning('Watch out!')
logging.error('Oh NO!')
logging.critical('x.x')

# format = "%(asctime)s - [%(levelname)s] [%(threadName)s] (%(module)s:%(lineno)d) %(message)s"

# logging.basicConfig(level=logging.INFO,
#                   format=format,)
