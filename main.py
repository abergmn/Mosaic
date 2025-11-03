from modules import full_scan
from modules import host_discovery
from modules import port_scan
from modules import banner_grab

from modules.utils import log_info
from colorama import init, Fore, Style

init(autoreset=True)

MENU_OPTIONS = {
    "1": ("Full scan (hosts + ports + banners)", full_scan, True),
    "2": ("Host discovery only", host_discovery, True),
    "3": ("Port scan only", port_scan, True),
    "4": ("Banner grabbing only", banner_grab, True),
    "q": ("Quit", None, False),
}

def choose_option() -> None:
    last_target = None

    while True:
        user_input = input(f"\n{Fore.GREEN}Enter choice (1-4, or q to quit)\n$> {Style.RESET_ALL}").strip().lower()

        if user_input == "":
            print(f"{Fore.RED}Please enter a choice.")
            continue

        if user_input not in MENU_OPTIONS:
            print(f"{Fore.RED}Invalid choice. Try again.")
            continue

        if user_input == "q":
            print(f"{Fore.MAGENTA}Goodbye.")
            return

        desc, func, needs_target = MENU_OPTIONS[user_input]

        target = None
        if needs_target:
            prompt = f"{Fore.YELLOW}Enter IP/Hostname"
            if last_target:
                prompt += f" (press Enter to reuse last {last_target})"
            prompt += f" {Style.RESET_ALL}"

            target_input = input(f"\n{prompt}\n$>").strip()
            if not target_input and last_target:
                target = last_target
                print(f"{Fore.GREEN}Using previous target:{Style.RESET_ALL} {target}")
            elif not target_input:
                print(f"{Fore.RED}Target required for this action.")
                continue
            else:
                target = target_input
                last_target = target

        try:
            if needs_target:
                func(target)
            else:
                func()
        except Exception as e:
            print(Fore.RED + f"Error running '{desc}': {e}")

        try_again = input(f"\n\n{Fore.YELLOW}Back to menu? (y/n)\n$> {Style.RESET_ALL}").strip().lower()
        if try_again in ("n", "no"):
            print(f"{Fore.MAGENTA}Exiting.")
            return

def print_ascii_art() -> None:
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
    print("  1. Full scan (hosts + ports + banners)")
    print("  2. Host discovery only")
    print("  3. Port scan only")
    print("  4. Banner grabbing only")

    print(f"========================================================================\n")

def main():
    log_info("Mosaic program start...")

    print_ascii_art()
    print_welcome_message()
    choose_option()

    log_info("Mosaic program end...")

if __name__ == "__main__":
    main()
