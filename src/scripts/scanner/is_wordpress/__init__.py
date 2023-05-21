# Py scanner
# A metasploit like tool but for scanning and retrieving data from websites.
# Github: https://www.github.com/awesomelewis2007/pyscan
# Licence: GNU General Public License v3.0
# By: Lewis Evans

from modules import log
import requests

description = "Checks if a server is using WordPress"

info = """Checks if a server is using WordPress
Variables:
NAME\tTYPE\tDESCRIPTION
HOST\tSTRING\tThe host(s) to scan (comma-separated)
TIMEOUT\tINTEGER\tThe timeout in seconds (default: 5)
PROTOCOL\tSTRING\tThe protocol to use (default: http)
"""


def run(variables, variables_data):
    if "HOST" in variables:
        hosts = variables_data[variables.index("HOST")].split(",")
    else:
        log.error("No host(s) provided.")
        return
    timeout = 5
    if "TIMEOUT" in variables:
        timeout = int(variables_data[variables.index("TIMEOUT")])
    try:
        if "PROTOCOL" in variables:
            protocol = variables_data[variables.index("PROTOCOL")]
        else:
            protocol = "http"
        for host in hosts:
            try:
                response = requests.get(f"{protocol}://{host.strip()}", timeout=timeout)
                if "wp-content" in response.text:
                    log.ok(f"Found WordPress on {host}")
                else:
                    log.error(f"WordPress not found on {host}")
            except requests.exceptions.RequestException:
                log.warn(f"Could not connect to {host.strip()}")
    except Exception as e:
        log.error(str(e))
