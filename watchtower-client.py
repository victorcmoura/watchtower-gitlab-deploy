#! /usr/local/bin/python3

import os
import requests
import logging
import click

logging.basicConfig(level=logging.DEBUG)
logging.info("Initializing Watchtower client for GitLabCI")

def validate_env(*args, **kwargs):
    for each in args:
        if len(each) == 0:
            logging.error(kwargs['error_message'])
            return 0
    return 1

TOKEN_NOT_SET_ERROR = '''
Failed authorization token retrieval.

Make sure that WATCHTOWER_API_TOKEN is set as an environment variable.

For more information, check the docs.
'''

HOSTNAME_NOT_SET_ERROR = '''
Failed hostname retrieval.

Make sure that WATCHTOWER_API_HOSTNAME is set as an environment variable.

For more information, check the docs.
'''

@click.command()
@click.option('--hostname', default="")
@click.option('--token', default="")
def run(hostname, token):    
    HOSTNAME = hostname
    TOKEN = token
    
    if (not validate_env(TOKEN, error_message=TOKEN_NOT_SET_ERROR)
       or not validate_env(HOSTNAME, error_message=HOSTNAME_NOT_SET_ERROR)):
        os._exit(1)
     
    logging.info("Attemting to run update at {0}".format(HOSTNAME))

    URL = "{}/v1/update".format(HOSTNAME)

    headers = {'Token': TOKEN}

    response = requests.get(URL, headers=headers)

    if response.status_code == 200:
        os._exit(0)

    os._exit(1)
if __name__ == "__main__":
    run()