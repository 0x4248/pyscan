# Py scanner
# A metasploit like tool but for scanning and retrieving data from websites.
# Github: https://www.github.com/awesomelewis2007/pyscan
# By: Lewis Evans

from modules import log
import requests

description = "Gets all links found on web pages"

info = """Gets all links found on web pages
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
        log.log("Connecting to the server " + f"{protocol}://{host}")
        response = requests.get(f"{protocol}://{host}")
        if response.status_code == 200:
            log.info(f"Web server found on {host}")
        else:
            log.warn(f"Web server not found on {host}")
            return

        links = []
        for line in response.text.split("\n"):
            if "<a href=" in line:
                link = line.split("<a href=")[1].split(">")[0].replace('"', "")
                if "." in link:
                    links.append(link)
        log.log(f"Found {len(links)} links")
        for link in links:
            log.log(f"Found {link}")
    except:
        log.warn(f"Could not connect to {host}")
        return
