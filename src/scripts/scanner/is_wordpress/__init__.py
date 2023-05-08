# Py scanner
# A metasploit like tool but for scanning and retrieving data from websites.
# Github: https://www.github.com/awesomelewis2007/pyscan
# By: Lewis Evans

from modules import log
import requests

description = "Checks if a server is using WordPress"

info = """Checks if a server is using WordPress
Variables:
NAME\tTYPE\tDESCRIPTION
HOST\tSTRING\tThe host to scan default: localhost)
TIMEOUT\tINTEGER\tThe timeout in seconds (default: 5)
PROTOCOL\tSTRING\tThe protocol to use (default: http)
"""


def run(variables, variables_data):
    host = "localhost"
    if "HOST" in variables:
        host = variables_data[variables.index("HOST")]
    timeout = 5
    if "TIMEOUT" in variables:
        timeout = int(variables_data[variables.index("TIMEOUT")])
    try:
        if "PROTOCOL" in variables:
            protocol = variables_data[variables.index("PROTOCOL")]
        else:
            protocol = "http"
        response = requests.get(f"{protocol}://{host}", timeout=timeout)
        if "wp-content" in response.text:
            log.ok(f"Found WordPress on {host}")
        else:
            log.info(f"WordPress not found on {host}")
    except:
        log.warn(f"Could not connect to {host}")
