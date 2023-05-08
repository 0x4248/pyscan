from modules import log
import requests
import os

description = "Download the files on a http file server"

info = """Download the files on a http file server
Variables:
NAME\tTYPE\tDESCRIPTION
HOST\tSTRING\tThe host and url to scan (default: localhost)
TIMEOUT\tINTEGER\tThe timeout in seconds (default: 5)
PROTOCOL\tSTRING\tThe protocol to use (default: http)
PATH\tSTRING\tThe path to download the content to (default: working directory)
"""


def run(variables, variables_data):
    host = "localhost"
    if "HOST" in variables:
        host = variables_data[variables.index("HOST")]

    timeout = 5
    if "TIMEOUT" in variables:
        timeout = int(variables_data[variables.index("TIMEOUT")])

    protocol = "http"
    if "PROTOCOL" in variables:
        protocol = variables_data[variables.index("PROTOCOL")]

    path = os.getcwd()
    if "PATH" in variables:
        path = variables_data[variables.index("PATH")]
        if not os.path.exists(path):
            log.fatal(f"Path {path} does not exist")
            return

    try:
        log.log("Connecting to the server " + f"{protocol}://{host}")
        response = requests.get(f"{protocol}://{host}", timeout=timeout)
        if "Index of" in response.text:
            log.ok(f"Found HTTP file server on {host}")
        else:
            log.info(f"HTTP file server not found on {host}")
            return

        files = []
        for line in response.text.split("\n"):
            if "<a href=" in line:
                link = line.split("<a href=")[1].split(">")[0].replace('"', "")
                if "." in link:
                    files.append(link)
        log.log(f"Found {len(files)} files")
        for file in files:
            log.log(f"Downloading {file}")
            response = requests.get(f"{protocol}://{host}/{file}", timeout=timeout)
            with open(f"{path}/{file}", "wb") as f:
                f.write(response.content)
    except:
        log.warn(f"Could not connect to {host}")
        return
