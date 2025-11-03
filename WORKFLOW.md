# Workflow

### Target Input
- User provides a single IP or hostname.
- If hostname, resolve it to a single canonical IP.
- IP Range Determination
- Based on the provided IP, determine the network range to scan.
> Example: a single IPv4 input defaults to a /24 network.


### Host Discovery
- Iterate over all IPs in the range.
- Quickly probe a few common ports (e.g., 80, 443) to detect active hosts.
- Store all active IPs in a list.


### Port Scanning
- For each active host, scan a predefined list of TCP ports.
- Record which ports are open and associate them with the host.


### Banner Grabbing
- For each open port, attempt to read a small banner.
- Store the banner if successfully grabbed.


### Result Compilation
- Return a list of active hosts.
- Each host includes its open ports and banners (if any).
