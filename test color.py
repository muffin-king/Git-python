from colorama import init
init()
5
from colorama import init, Fore, Back, Style
init(convert=True)
print(Fore.RED + 'some red text') 
print(Back.GREEN + 'and with a green background') 
print(Style.DIM + 'and in dim text') 
print(Style.RESET_ALL) 
print('back to normal now') 
