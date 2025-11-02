"""
NOTE: Basic workflow is as follows
        > Get target input (IPv4 addr or hostname)
        > Find active hosts within target
        > Find active ports within active host
        > Try to grab banner for each active host
        > Compile results into JSON file 'data.json'
"""

from modules.utils import log_error
from modules.utils import log_info

def main():
    log_info("Mosaic program start...")

    # ...

    log_info("Mosaic program end...")
    
    return

if __name__ == "__main__":
    main()
