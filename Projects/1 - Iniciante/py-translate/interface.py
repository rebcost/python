from rich.console import Console
from os import system
console = Console()

def logo():
    logo = """ 

    ___         _____               _       _             
    / _ \_   _  /__   \_ __ __ _  __| |_   _| |_ ___  _ __ 
    / /_)/ | | |   / /\/ '__/ _` |/ _` | | | | __/ _ \| '__|
    / ___/| |_| |  / /  | | | (_| | (_| | |_| | || (_) | |   
    \/     \__, |  \/   |_|  \__,_|\__,_|\__,_|\__\___/|_|   
        |___/                                             


    """
    system("clear")
    console.print(logo, style="green")

def menu():
    console.print("\n\n\n")
    console.print("[1] - Traduzir Português para Inglês")
    console.print("[2] - Traduzir Inglês para Português\n")
    console.print("[0] - SAIR")
    console.print("\n\n")
    console.print("Escolha entre as opções acima: ")

def mostrar_formatado(txt):
    console.print(f"[green]{txt}[/]")