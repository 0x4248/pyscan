import colorama

def ok(message):
    print(f"{colorama.Fore.GREEN}[+]{colorama.Fore.RESET} {message}")

def info(message):
    print(f"{colorama.Fore.BLUE}[i]{colorama.Fore.RESET} {message}")

def log(message):
    print(f"{colorama.Fore.CYAN}[*]{colorama.Fore.RESET} {message}")

def warn(message):
    print(f"{colorama.Fore.YELLOW}[!]{colorama.Fore.RESET} {message}")

def error(message):
    print(f"{colorama.Fore.RED}[-]{colorama.Fore.RESET} {message}")

def fatal(message):
    print(f"{colorama.Fore.RED}[x]{colorama.Fore.RESET} {message}")

def question(message):
    print(f"{colorama.Fore.YELLOW}[?]{colorama.Fore.RESET} {message}")
