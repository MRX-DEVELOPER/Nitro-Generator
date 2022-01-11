import os
import ctypes
import requests
import random
import string
import time
print("""


               | \ | (_) __ _| |__ | |_| |/ (_) | | ___ _ __ 
               |  \| | |/ _` | '_ \| __| ' /| | | |/ _ \ '__|
               | |\  | | (_| | | | | |_| . \| | | |  __/ |   
               |_| \_|_|\__, |_| |_|\__|_|\_\_|_|_|\___|_|   
                        |___/                                
╔═══════════════════════╦══════════════════════════╦═══════════════════════╗
║  Dev : !NightKiller   ║  Info  : Nitro Generator ║  Programm  : Python   ║
╚═══════════════════════╩══════════════════════════╩═══════════════════════╝



""")
time.sleep(0.1)
print("NIGHTKILLER GENERATOR")
time.sleep(0.1)
print("THE FASTEST NITRO GEN IN THE WORLD .\n")
time.sleep(0.1)

num = int(input('Input How Many Codes to Generate and Check: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Please wait ...")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valid | {nitro} ")
            break
        else:
            print(f" Invalid | {nitro} ")


print("Discord : https://discord.gg/9YFRGEfNCn\n")

time.sleep(0.2)

input("\nCodes generated !! If Valide codes.txt is empty retry to gen 20 millions code ;) ")

