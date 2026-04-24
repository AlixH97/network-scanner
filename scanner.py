
#!/usr/bin/env python3
"""
Network Scanner Tool
Author: Ali Hussnain
Description: Scans a network range, detects live hosts, open ports, and services.
             Outputs a clean terminal report and saves results to a JSON file.
"""

import nmap
import json
import datetime
import sys
import socket


def get_hostname(ip):
    """Try to resolve IP to hostname."""
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Unknown"


def scan_network(target, ports="22,80,443,3389,8080,21,23,25,53,110,139,445"):
    """
    Scan a target IP or range for live hosts and open ports.
    
    Args:
        target (str): IP address or range e.g. '192.168.1.0/24' or '192.168.1.1'
        ports (str): Comma-separated port list or range e.g. '1-1024'
    
    Returns:
        dict: Scan results
    """
    nm = nmap.PortScanner()

    print(f"\n{'='*60}")
    print(f"  🔍 NETWORK SCANNER - Starting Scan")
    print(f"{'='*60}")
    print(f"  Target  : {target}")
    print(f"  Ports   : {ports}")
    print(f"  Time    : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")
    print("  Scanning... this may take a moment.\n")

    # Run the scan: -sV for service/version detection, -T4 for faster timing
    nm.scan(hosts=target, ports=ports, arguments="-sV -T4 --open")

    results = {
        "scan_info": {
            "target": target,
            "ports_scanned": ports,
            "timestamp": datetime.datetime.now().isoformat(),
            "total_hosts_scanned": len(nm.all_hosts()),
        },
        "hosts": []
    }

    live_hosts = 0

    for host in nm.all_hosts():
        state = nm[host].state()
        if state != "up":
            continue

        live_hosts += 1
        hostname = get_hostname(host)

        host_data = {
            "ip": host,
            "hostname": hostname,
            "state": state,
            "open_ports": []
        }

        print(f"  {'─'*50}")
        print(f"  🖥️  Host     : {host}")
        print(f"  📛 Hostname : {hostname}")
        print(f"  ✅ Status   : {state.upper()}")

        # Check TCP ports
        if "tcp" in nm[host]:
            print(f"  📡 Open Ports:")
            for port, data in nm[host]["tcp"].items():
                if data["state"] == "open":
                    service = data.get("name", "unknown")
                    version = data.get("version", "")
                    product = data.get("product", "")
                    full_service = f"{product} {version}".strip() or service

                    port_data = {
                        "port": port,
                        "protocol": "tcp",
                        "service": service,
                        "version": full_service
                    }
                    host_data["open_ports"].append(port_data)

                    print(f"      Port {port}/tcp  →  {service.upper():<12} {full_service}")

        if not host_data["open_ports"]:
            print("      No open ports found on scanned ports.")

        results["hosts"].append(host_data)

    results["scan_info"]["live_hosts"] = live_hosts

    print(f"\n  {'─'*50}")
    print(f"\n{'='*60}")
    print(f"  📊 SCAN SUMMARY")
    print(f"{'='*60}")
    print(f"  Hosts scanned : {results['scan_info']['total_hosts_scanned']}")
    print(f"  Live hosts    : {live_hosts}")
    print(f"{'='*60}\n")

    return results


def save_report(results, filename=None):
    """Save scan results to a JSON file."""
    if not filename:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"scan_report_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(results, f, indent=4)

    print(f"  💾 Report saved to: {filename}\n")
    return filename


def main():
    # Default target — change this to your local network range
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        # Default: scan localhost for demo purposes
        target = "127.0.0.1"
        print(f"  ℹ️  No target provided. Usage: python3 scanner.py <target>")
        print(f"  ℹ️  Example: python3 scanner.py 192.168.1.0/24")
        print(f"  ℹ️  Defaulting to localhost scan...\n")

    ports = sys.argv[2] if len(sys.argv) > 2 else "22,80,443,3389,8080,21,23,25,53,110,139,445"

    results = scan_network(target, ports)
    save_report(results)


if __name__ == "__main__":
    main()





