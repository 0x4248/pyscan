# Py scanner
# A metasploit like tool but for scanning and retrieving data from websites.
# Github: https://www.github.com/awesomelewis2007/pyscan
# By: Lewis Evans

from modules import log
import requests

description = "Gets information about the site"

info = """Gets information about the site
Variables:
NAME\tTYPE\tDESCRIPTION
HOST\tSTRING\tThe host and url to scan (default: localhost)
PROTOCOL\tSTRING\tThe protocol to use (default: http)
"""


def run(variables, variables_data):
    host = "localhost"
    if "HOST" in variables:
        host = variables_data[variables.index("HOST")]

    protocol = "http"
    if "PROTOCOL" in variables:
        protocol = variables_data[variables.index("PROTOCOL")]

    try:
        print(f"Host: {host}")
        response = requests.get(f"{protocol}://{host}")
        print(f"Code: {response.status_code}")
        print(f"Headers: {response.headers}")
        if "Server" in response.headers:
            print(f"Server: {response.headers['Server']}")
        else:
            print("Server: OTHER")
        if "X-Powered-By" in response.headers:
            print(f"Webserver: {response.headers['X-Powered-By']}")

        if "wp-content" in response.text:
            print("Using WordPress")

    except:
        log.warn(f"Could not connect to {host}")
