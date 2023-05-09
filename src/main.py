# Py scanner
# A metasploit like tool but for scanning and retrieving data from websites.
# Github: https://www.github.com/awesomelewis2007/pyscan
# By: Lewis Evans

import os
import sys
import importlib
import modules.log as log
from colorama import Fore, Back, Style

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from scripts import *

def run_script(script_name, variables, variables_data):
    name = script_name.replace("src/", "").replace("/", ".").replace(".py", "")
    script = importlib.import_module(name)
    script.run(variables, variables_data)


def get_script_info(script_name):
    name = script_name.replace("src/", "").replace("/", ".").replace(".py", "")
    script = importlib.import_module(name)
    return script.info


def get_script_description(script_name):
    name = script_name.replace("src/", "").replace("/", ".").replace(".py", "")
    script = importlib.import_module(name)
    return script.description


def count_scripts():
    count = 0
    for root, dirs, files in os.walk("src/scripts"):
        for name in files:
            if name.endswith(".py"):
                count += 1
    return count


def print_help():
    print("Available commands:")
    print("help - Print this help message")
    print("exit - Exit the program")
    print("list - List all available scripts")
    print("use <script> - Use a script")
    print("set <variable> <value> - Set a variable")
    print("info - Print information about the current script")
    print("run - Run the current script")
    print("search <query> - Search for a script")


def list_scripts(print_scripts=True):
    scripts = []
    count = 0
    for root, dirs, files in os.walk("src/scripts"):
        for name in files:
            if name.endswith(".py"):
                scripts.append(os.path.join(root, name))
                if print_scripts:
                    print(f"{count}\t{os.path.join(root, name)}")
                count += 1
    return scripts


def search_scripts(query):
    scripts = []
    count = 0
    for root, dirs, files in os.walk("src/scripts"):
        for name in files:
            if name.endswith(".py"):
                scripts.append(os.path.join(root, name))
                print(
                    f"{count}\t{os.path.join(root, name).replace(query, Fore.BLUE + query + Fore.RESET)}"
                )
                count += 1
    return scripts


def welcome():
    print("Welcome to py-scan!")
    print("There are " + str(count_scripts()) + " scripts available")
    print("Type help for a list of commands")


def terminal():
    welcome()
    last_result = []
    current_script = ""
    variables = []
    variables_data = []
    while True:
        if current_script == "":
            command = input("py-scan> ")
        else:
            command = input(
                "py-scan("
                + Fore.BLUE
                + current_script.replace("src/scripts/", "")
                + Fore.RESET
                + ")> "
            )
        if command == "exit" or command == "quit":
            sys.exit(0)

        elif command == "help":
            print_help()

        elif command == "list":
            last_result = list_scripts()

        elif command.startswith("search"):
            last_result = search_scripts(command.split(" ")[1])

        elif command.startswith("use"):
            if command.split(" ")[1].isdigit():
                script = last_result[int(command.split(" ")[1])]
                if os.path.isfile(script):
                    current_script = script
                else:
                    log.error("Script not found")
            else:
                script = command.split(" ")[1]
                if os.path.isfile(script):
                    current_script = script
                else:
                    log.error("Script not found")

        elif command.startswith("set"):
            variable = command.split(" ")[1].upper()
            value = command.split(" ")[2]
            print(variable + " => " + value)
            if variable in variables:
                variables_data[variables.index(variable)] = value
            else:
                variables.append(variable)
                variables_data.append(value)

        elif command.startswith("get"):
            variable = command.split(" ")[1]
            if variable == "*":
                for i in range(len(variables)):
                    print(variables[i] + "\t" + variables_data[i])
            elif variable in variables:
                print(variables_data[variables.index(variable)])
            else:
                log.error("Variable not found")

        elif command == "info":
            if current_script == "":
                log.error("No script selected")
            else:
                print(get_script_info(current_script))

        elif command == "run" or command == "scan":
            if current_script == "":
                log.error("No script selected")
            else:
                run_script(current_script, variables, variables_data)
        else:
            os.system(command)

if __name__ == "__main__":
    terminal()
