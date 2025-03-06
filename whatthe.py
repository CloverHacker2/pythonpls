from requests import get
from colorama import Fore, Back, Style

ip = get('https://raw.githubusercontent.com/CloverHacker2/CloverHacker2.github.io/refs/heads/main/coco').text
print(Fore.LIGHTYELLOW_EX + ip)
print(Fore.RESET)