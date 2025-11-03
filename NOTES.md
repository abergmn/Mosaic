# Notes
- first print/input statement of function under `modules/` must begin with `\n`
- each file under `modules/` serves as the main function containing the process of an option
    + some functions require 'helper' functions (additional tools or functions which one or more modules depend on)
    + Ex: `full_scan.py` contains the function `full_scan()` where it's job is to perform all functions relating to scanning/information collection, this function would require helper functions needed by `banner_grab.py`.
