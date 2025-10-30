BLUE = "\033[1;34m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"


def info(message: str):
    """Print informational messages in blue."""
    print(f"{BLUE}INFO{RESET}  {message}")

def error(message: str):
    """Print error messages in red."""
    print(f"{RED}ERROR{RESET} {message}")

def success(message: str):
    """Print success messages in green."""
    print(f"{GREEN}SUCCESS{RESET} {message}")
    

