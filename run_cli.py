from src import cli, cli_logging
import logging

cli_logging.set_logging()
    
# logging.info('qtfirebase cli quit sucessfully')
logging.critical('qtfirebase cli had a big ouch')
exit(0)
cli.run([])
