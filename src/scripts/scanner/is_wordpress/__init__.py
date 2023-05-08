from modules import log
import requests

description = "Checks if a server is using WordPress"

info = """Checks if a server is using WordPress
Variables:
NAME\tTYPE\tDESCRIPTION
HOST\tSTRING\tThe host to scan default: localhost)
PORT\tINTEGER\tThe port to scan (default: 80)
TIMEOUT\tINTEGER\tThe timeout in seconds (default: 5)
PROTOCOL\tSTRING\tThe protocol to use (default: http)
"""


def run(variables, variables_data):
    host = "localhost"
    if "HOST" in variables:
        host = variables_data[variables.index("HOST")]
    port = 80
    if "PORT" in variables:
        port = int(variables_data[variables.index("PORT")])
    timeout = 5
    if "TIMEOUT" in variables:
        timeout = int(variables_data[variables.index("TIMEOUT")])
    try:
        if "PROTOCOL" in variables:
            protocol = variables_data[variables.index("PROTOCOL")]
        else:
            protocol = "http"
        response = requests.get(f"{protocol}://{host}:{port}", timeout=timeout)
        if "wp-content" in response.text:
            log.ok(f"Found WordPress on {host}:{port}")
        else:
            log.info(f"WordPress not found on {host}:{port}")
    except:
        log.warn(f"Could not connect to {host}:{port}")
