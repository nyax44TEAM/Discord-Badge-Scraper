from discordsc.nyax44 import scrape
import os

try:
    from colorama import Fore
except:
    os.system('pip install colorama && cls')
    from colorama import Fore

try:
    import json
except:
    os.system('pip install json && cls')
    import json

x = [
    "f",
    "F",
    "n",
    "N"
]

def bannerZ():
    print(Fore.LIGHTMAGENTA_EX + 
        """
        ██████╗░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░  ░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗██████╗░
        ██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
        ██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║  ╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝█████╗░░██████╔╝
        ██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║  ░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
        ██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝  ██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░███████╗██║░░██║
        ╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
        """
         + Fore.RESET)

def main():

    token = input(Fore.LIGHTCYAN_EX + "[+] Enter your token (skip to choose from config): " + Fore.RESET)

    if len(token) < 10:
        with open("config.json", "r", encoding="utf-8") as ff:
            config = json.load(ff)
            token = config["token"]

    guild_id = input(Fore.LIGHTCYAN_EX + "Enter guild id: " + Fore.RESET)
    channel_id = input(Fore.LIGHTCYAN_EX + "Enter channel id: " + Fore.RESET)

    run_badge_scraper = input(Fore.LIGHTCYAN_EX + "Run badge scraper (True/False)? " + Fore.RESET)

    if run_badge_scraper != "False" or run_badge_scraper != "True":
        for y in x:
            if y in run_badge_scraper:
                run_badge_scraper = "False"
                break
            else:
                run_badge_scraper = "True"
    run_badge_scraper = bool(run_badge_scraper)

    ids = scrape(token, guild_id, channel_id, run_badge_scraper)

    print(f"{Fore.GREEN}[SUCCESS] Successfuly scraped {len(ids)} IDs from {guild_id} saving them to scraped/{guild_id}.txt" + Fore.RESET)

    with open(f"./scraped/{guild_id}.txt", "w", encoding="utf-8") as f:
        for id in ids:
            print(id)
            f.write(f"{id}\n")

    input(Fore.LIGHTCYAN_EX + "Press enter to Exit...\n\n" + Fore.RESET)

main()
