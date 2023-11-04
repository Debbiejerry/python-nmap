import nmap

# creating an instance of the scanner
nm = nmap.PortScanner()

target = "45.33.32.156"
options = "-sV -sC scan_results"

# calling the scan method on the instance of the the nmap.PortScanner class. The scan method is basically used to perform a network scan using nmap
nm.scan(target, arguments=options)

for host in nm.all_hosts():
    print("Host: % (%s)" % (host, nm[host].hostname()))
    print("State: %" % nm[host].state())
    for protocol in nm[host].all_protocols():
        print("Protocol %" % protocol)
        port_info = nm[host][protocol]
        for port, state in port_info.items():
            print("Port: %s\tState: %s" % (port, state))
