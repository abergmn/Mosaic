"""
handle_im.py

Handle the input menu!!!!!!
"""

from . import full_scan, host_discovery, port_scan, banner_grab, resolve_target
from .utils import log_error, log_info

from colorama import init, Fore, Style
from typing import Optional

init(autoreset=True)

def ui_print_ascii_art() -> None:
    print(f"\n========================================================================")
    print(f"\t{Fore.CYAN}$$\\      $$\\                               $$\\           {Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}$$$\\    $$$ |                              \\__|          {Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}$$$$\\  $$$$ | $$$$$$\\   $$$$$$$\\  $$$$$$\\  $$\\  $$$$$$$\\ {Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}$$\\$$\\$$ $$ |$$  __$$\\ $$  _____| \\____$$\\ $$ |$$  _____|{Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}$$ \\$$$  $$ |$$ /  $$ |\\$$$$$$\\   $$$$$$$ |$$ |$$ /      {Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}$$ |\\$  /$$ |$$ |  $$ | \\____$$\\ $$  __$$ |$$ |$$ |      {Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}$$ | \\_/ $$ |\\$$$$$$  |$$$$$$$  |\\$$$$$$$ |$$ |\\$$$$$$$\\ {Style.RESET_ALL}")
    print(f"\t{Fore.CYAN}\\__|     \\__| \\______/ \\_______/  \\_______|\\__| \\_______|{Style.RESET_ALL}")
    print(f"========================================================================\n")

def print_welcome_message() -> None:
    print(f"{Fore.GREEN}Welcome to Mosaic!{Style.RESET_ALL}\n")

    print("Mosaic is a source-available Python project for network reconnaissance")
    print("and mapping. It helps collect network intelligence and organize it")
    print("into a clear, comprehensible view.\n")
    
    print(f"{Fore.YELLOW}⚠️ Note:{Style.RESET_ALL} Currently in proof-of-concept / development stage.")
    print("Use only on systems you own or have explicit permission to test.\n")

    print(f"{Fore.MAGENTA}Workflow:{Style.RESET_ALL}")
    print("  1. Enter a target (IPv4 address, subnet, or hostname)")
    print("  2. Find active hosts within the target")
    print("  3. Scan active ports for each host")
    print("  4. Attempt to grab banners from active services")
    print("  5. Save results to a JSON file ('data.json')\n")

    print(f"{Fore.BLUE}Example targets:{Style.RESET_ALL}")
    print("  - Single host: 192.168.1.10")
    print("  - Subnet: 192.168.1.0/24")
    print("  - Hostname: example.com\n")

    print(f"{Fore.CYAN}Available scan modes:{Style.RESET_ALL}")
    # print menu options
    for k, (desc, _, _) in MENU_OPTIONS.items():
        print(f"  {k}. {desc}")

    print(f"\n========================================================================\n")

def get_target(last_target: Optional[str]) -> Optional[str]:
    prompt = "Enter IP/Hostname"
    if last_target:
        prompt += f" (press Enter to reuse last {last_target})"
    target_input = input(f"\n{prompt}\n$>").strip()
    if not target_input and last_target:
        print(f"Using previous target: {last_target}")
        return last_target
    if not target_input:
        print("Target required for this action.")
        return None
    return target_input

MENU_OPTIONS = {
    "1": ("Full scan (hosts + ports + banners)", full_scan, True),
    "2": ("Host discovery", host_discovery, True),
    "3": ("Port/Ports(s) scan", port_scan, True),
    "4": ("Banner grabber", banner_grab, True),
    "5": ("Resolve IP/Hostname", resolve_target, True),
    "q": ("Quit", None, False),
}

def menu_choose_option() -> None:
    last_target = None

    while True:
        user_input = input(f"\n{Fore.GREEN}Enter choice (1-4, or q to quit)\n$> {Style.RESET_ALL}").strip().lower()

        # no input
        if user_input == "":
            print(f"{Fore.RED}Please enter a choice.")
            continue

        # user wants out
        if user_input in ("q", "quit", "exit"):
            print(f"{Fore.MAGENTA}Goodbye.")
            return

        # invalid option
        if user_input not in MENU_OPTIONS:
            print(f"{Fore.RED}Invalid choice. Try again.")
            continue

        desc, func, needs_target = MENU_OPTIONS[user_input]
        target = None

        # NOTE: basically just to account for quitting + adding ability to reuse last input...
        #       options by default should require an argument
        if needs_target:
            target = get_target(last_target)
        if not target:
            continue
        last_target = target

        try:
            if needs_target:
                func(target)
            else:
                func()
        except Exception as e:
            print(f"{Fore.RED}Error running '{desc}': {e}")

        print(f"\n{'-' * 70}\n")

def handle_im() -> None:
    ui_print_ascii_art()
    print_welcome_message()

    # allow Ctrl+C exit
    try:
        menu_choose_option()
    except KeyboardInterrupt:
        print()
        log_info("Interrupted. Exiting cleanly.")
