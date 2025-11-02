# Mosaic

**Mosaic** is a source-available Python project designed for **network reconnaissance and mapping**. Its goal is to collect network intelligence and organize it into a clear, comprehensible view.

> ⚠️ Currently in **proof-of-concept / development stage**. Use responsibly and only on systems you own or have explicit permission to test.

---

## Features (Current / Planned)
- **Network Discovery:** Identify live hosts in a subnet via ping sweeps.
- **Port Scanning:** Scan a host or range of hosts to identify open TCP ports.
- **Banner Grabbing:** Attempt to collect service banners from open ports.
- **Data Mapping (Future):** Organize collected information into a structured network map.

---

## Installation
Mosaic is currently a simple Python project; no packaging is required.

Clone the repository:
```bash
git clone <repo-url>
cd mosaic
```

## Usage
Run Mosaic from the command line <!--with the target host or subnet-->:
```bash
python main.py
```
<!-- python main.py --target <host/subnet> -->

---

## Responsible Use
Mosaic is a network reconnaissance tool. Unauthorized scanning or testing of systems you do not own or have explicit permission to test is illegal and prohibited. Use responsibly.

## License & Contribution Notice
Mosaic is published as **source-available** software. You are welcome to use Mosaic and to submit improvements via pull requests, but the source code is **not** public domain nor freely redistributable for others to republish as their own work.

Key points:
- You may run and use Mosaic subject to the terms in [`LICENSE.txt`](LICENSE.txt).
- Contributions are accepted only under the project’s [Contributor License Agreement](CONTRIBUTOR_LICENSE_AGREEMENT.md) (see [`CONTRIBUTING.md`](CONTRIBUTING.md)).
- You may **not** remove or alter copyright or attribution notices, claim Mosaic (or parts of it) as your original work, or redistribute the source code as your own.
