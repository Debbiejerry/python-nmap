# python-nmap
# Python Nmap Network Scanner

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## Introduction

The Python Nmap Network Scanner is a simple script that uses the `nmap` library to perform network scans on a specified target. This tool can provide information about open ports, services running on those ports, and more. It's a valuable resource for network administrators and security professionals.

## Features

- Port Scanning: The script can scan a target for open ports.
- Service Detection: It can detect the services running on the open ports.
- Host Information: It provides information about the target host and its state.

## Getting Started

To get started with the Python Nmap Network Scanner, follow these instructions:

### Prerequisites

- Python 3.x
- The `python-nmap` library, which you can install using `pip install python-nmap`.
- Nmap, which should be installed on your system.

### Usage

1. Import the `nmap` library.

2. Create an instance of the Nmap scanner:

   nm = nmap.PortScanner()
   
4. Define the target IP address or hostname and the Nmap scan options:
   target = "45.33.32.156"
   options = "-sV -sC"

5. Call the scan method on the instance of the nmap.PortScanner class to perform the network scan:
   nm.scan(target, arguments=options)
   
7. Iterate through the results to display information about the scanned host, state, protocols, ports, and their states.
   for host in nm.all_hosts():
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    for protocol in nm[host].all_protocols():
        print("Protocol: %s" % protocol)
        port_info = nm[host][protocol]
        for port, state in port_info.items():
            print("Port: %s\tState: %s" % (port, state))

## Contributing
Contributions to this project are welcome. To contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Test your changes.
5. Create a pull request with a clear description of your changes.
