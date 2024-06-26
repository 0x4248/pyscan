# Py scanner
# A metasploit like tool but for scanning and retrieving data from websites.
# Github: https://www.github.com/0x4248/pyscan
# Licence: GNU General Public License v3.0
# By: 0x4248

from modules import log

description = "Prints hello world"

info = """Prints hello world to the console
Variables:
NAME\tTYPE\tDESCRIPTION
NAME\tSTRING\tThe name to print (default: world)
"""


def run(variables, variables_data):
    name = "world"
    if "NAME" in variables:
        name = variables_data[variables.index("NAME")]
    log.log(f"Hello {name}")
