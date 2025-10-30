import requests
import threading
import itertools
import time
import sys
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
    

#def loading(message: str = "Loading..."):
 #   """Show a temporary loading spinner before an action."""
  ## print(f"{YELLOW}LOADING{RESET}  {message}", end="", flush=True)
   # for _ in range(10):  # adjust number for longer loading effect
    #    for frame in spinner:
     #       sys.stdout.write(f"\r{YELLOW}LOADING{RESET}  {message} {frame}")
      #      sys.stdout.flush()
       #     time.sleep(0.1)
   # sys.stdout.write("\r") 