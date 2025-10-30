from modules import discover_hosts
from modules import scan_host
from modules import grab_banner

# brain storming.....

# what variables are shared between functions?
# how to best represent all of this data?
# Ex: active ports relate to active hosts... each host has active ports... each port must have a host associated with it...


possible_hosts = None # range of possible IPs within a subnet
active_hosts = []
active_ports = []


for host in possible_hosts:
    # check if host is online
    # if is online, add to active_hosts
    None

for host in active_hosts:
    # scan ports, if port is active, add to lists of active ports
    None

for ports in active_ports:
    # grab banner
    None

def main():
    # workflow: discover -> scan -> grab banners
    return

if __name__ == "__main__":
    main()
