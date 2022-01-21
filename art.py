import time


logo = """
MMMMMMMMMMMMMMWXKXNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMWN0dlclooxkOKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMWKklcokKK0kxdollodxkOKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMWXOdclxKNMMMMMMWNXK0kxdollodxk0KXNWMMMMMMMMMMMMMMMMMMNOkO0XNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMXxlcdOXWMMMMMMMMMMMMMMMWNXKOkxdlllodxO0KNWWMMMMMMMMMMWKo;;:clodkOKXNWWMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMWO:;cx0KXNWMMMMMMMMMMMMMMMMMMMMWNX0OkdolllodxOKNMMMMMMMKl;;;;;;;;;:cloxkOKXNWMMMMMMMMMMMMMMMMMMM
MMMMWOc;;;;:codxO0KXWWMMMMMMMMMMMMMMMMMMMWWNX0OdcclOWMMMMMMKl;;;;;;;;;;;;;;;;:cldxkOKXNWWMMMMMMMMMMM
MMMMWO:;;;;;;;;;;::codxO0KNWWMMMMMMMMMMMMMMMMMMXo:cOWMMMMMMKo;;;;;;;;;;;;;;;;;;;;;;;:cldxk0KXWMMMMMM
MMMMWO:;;;;;;;;;;;;;;;;;::lodkO0XNWWMMMMMMMMMMMXo:cOWMMMMMMKl;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:cxNMMMMM
MMMMWO:;;;;;;;;;;;;;;;;;;;;;;;;:clodkOKNMMMMMMMXo:cOWMMMMMMKl;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oXMMMMM
MMMMWO:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;cOWMMMMMMXo:cOWMMMMMMKl;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oXMMMMM
MMMMWO:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:kWMMMMMMXo:cOWMMMMMMKl;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oXMMMMM
MMMMWO:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:kWMMMMMMXo:cOWMMMMMMKl;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oXMMMMM
MMMMWO:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:kWMMMMMMXo:cOWMMMMMMKl;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oXMMMMM
MMMMWO:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:kWMMMMMMXo:cOWMMMMMMKl;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oXMMMMM
MMMMWO:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:kWMMMMMMXo:cOWMMMMMMKl;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oXMMMMM
MMMMWO:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:kWMMMMMMXo:cOWMMMMMMKl;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oXMMMMM
MMMMWO:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:kWMMMMMMXo:cOWMMMMMMKl;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oXMMMMM
MMMMWO:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:kWMMMMMMXo:cOWMMMMMMKl;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oXMMMMM
MMMMWO:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:kWMMMMMMXo:cOWMMMMMMKl;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oXMMMMM
MMMMWO:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:kWMMMMMMXo:cOWMMMMMMKl;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oXMMMMM
MMMMWO:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:kWMMMMMMXo:cOWMMMMMMKl;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oXMMMMM
MMMMWO:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:kWMMMMMMXo:cOWMMMMMMKl;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oXMMMMM
MMMMWO:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:kWMMMMMMXo:cOWMMMMMMKo;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oXMMMMM
MMMMWO:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:kWMMMMMMXo:cOWMMMMMMKl;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oXMMMMM
MMMMWOc;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:kWMMMMMMXo:cOWMMMMMWKl;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oXMMMMM
MMMMWOc;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:kWMMMMMMXo:ckWMMMMMMXxl::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;oXMMMMM
MMMMWOc;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:kWMMMMMMXo:ckWMMMMMMMWNK0kxdoc:;;;;;;;;;;;;;;;;;;;;;;;oXMMMMM
MMMMMXkdoc::;;;;;;;;;;;;;;;;;;;;;;;;;;:kWMMMMMMXo:ckWMMMMMMMMMMMMMWNXK0kxdlc:;;;;;;;;;;;;;;;;oXMMMMM
MMMMMMMWNXK0kxolc:;;;;;;;;;;;;;;;;;;;;:kWMMMMMMXo:ckNWMMMMMMMMMMMMMMMMMMMWNXKOkxdlc:;;;;;;;;;oXMMMMM
MMMMMMMMMMMMMMWNXKOkxolc:;;;;;;;;;;;;;:kWMMMMMMXd::codkOKXNWWMMMMMMMMMMMMMMMMMMMWNXKOkxolc:;;oXMMMMM
MMMMMMMMMMMMMMMMMMMMMWNXKOkxolc:;;;;;;:kWMMMMMMWNKK0kxdlllloxkOKXNWWMMMMMMMMMMMMMMMMMMWWXOo::dNMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWWNX0OkdolccOWMMMMMMMMMMMMMWNXKOkxolllloxkOKXNWMMMMMMMMMMMMNKxlcokXWMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNKKXMMMMMMMMMMMMMMMMMMMMWWNX0Okdolllodxk0KXNWWWWXOoclxKNWMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNX0OkdolllodxkdlcdOXWMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNX0OkdodkKWMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNWWMMMMMMMMMMMMMMM
"""

books_online = """

██████╗░░█████╗░░█████╗░██╗░░██╗░██████╗        ░█████╗░███╗░░██╗██╗░░░░░██╗███╗░░██╗███████╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝        ██╔══██╗████╗░██║██║░░░░░██║████╗░██║██╔════╝
██████╦╝██║░░██║██║░░██║█████═╝░╚█████╗░        ██║░░██║██╔██╗██║██║░░░░░██║██╔██╗██║█████╗░░
██╔══██╗██║░░██║██║░░██║██╔═██╗░░╚═══██╗        ██║░░██║██║╚████║██║░░░░░██║██║╚████║██╔══╝░░
██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗██████╔╝        ╚█████╔╝██║░╚███║███████╗██║██║░╚███║███████╗
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░        ░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝╚═╝░░╚══╝╚══════╝

                    ░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗██████╗░
                    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
                    ╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝█████╗░░██████╔╝
                    ░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
                    ██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░███████╗██║░░██║
                    ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝"""


def welcome():
    print(logo)
    time.sleep(1)
    print()
    print()
    try:
        print(books_online)
    except UnicodeEncodeError:
        print("-" * 100)
    time.sleep(1)
    print()
    print("-" * 100)
    print()
    time.sleep(0.8)
    print(" - - - - Ready to run!!!")
    time.sleep(0.2)
    print()

