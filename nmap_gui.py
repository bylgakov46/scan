from tkinter import *
import json
import nmap3

root = Tk()
root.title('Nmap Scanning Tool')

host_label = Label(root, text='Host IP or Domain:')
host_entry = Entry(root)

scan_label = Label(root, text='Pick scan type:')
scan_options = ['OS Scan',
                'Top Ports',
                'Version Scan',
                'List Scan',
                'Subnet Scan',
                'DNS Brute Scan',
                'Ping Scan']
scan_selected = StringVar(root)
scan_select = OptionMenu(root, scan_selected, *scan_options)


def scan():
    nmap = nmap3.Nmap()
    nmap1 = nmap3.NmapScanTechniques()
    scan_type = scan_selected.get()
    if scan_type == 'OS Scan':
        os_results = nmap.nmap_os_detection(host_entry.get())
        with open('OS_Scan.json', 'w') as file:
            file.write(json.dumps(os_results))
        success_label = Label(root, text='Scan Completed!')
        success_label.grid_forget()
        success_label.grid(row=2, column=0)

    elif scan_type == 'Top Ports':
        top_ports = nmap.scan_top_ports(host_entry.get())
        with open('Top_Ports.json', 'w') as file:
            file.write(json.dumps(top_ports))
        success_label = Label(root, text='Scan Completed!')
        success_label.grid_forget()
        success_label.grid(row=2, column=0)

    elif scan_type == 'Version Scan':
        version_scan = nmap.nmap_version_detection(host_entry.get())
        with open('Version_Scan.json', 'w') as file:
            file.write(json.dumps(version_scan))
        success_label = Label(root, text='Scan Completed!')
        success_label.grid_forget()
        success_label.grid(row=2, column=0)

    elif scan_type == 'List Scan':
        version_scan = nmap.nmap_list_scan(host_entry.get())
        with open('List_scan.json', 'w') as file:
            file.write(json.dumps(version_scan))
        success_label = Label(root, text='Scan Completed!')
        success_label.grid_forget()
        success_label.grid(row=2, column=0)

    elif scan_type == 'Subnet Scan':
        version_scan = nmap.nmap_subnet_scan(host_entry.get())
        with open('Subnet_Scan.json', 'w') as file:
            file.write(json.dumps(version_scan))
        success_label = Label(root, text='Scan Completed!')
        success_label.grid_forget()
        success_label.grid(row=2, column=0)

    elif scan_type == 'DNS Brute Scan':
        version_scan = nmap.nmap_dns_brute_script(host_entry.get())
        with open('DNS_brute_scan.json', 'w') as file:
            file.write(json.dumps(version_scan))
        success_label = Label(root, text='Scan Completed!')
        success_label.grid_forget()
        success_label.grid(row=2, column=0)

    elif scan_type == 'Ping Scan':
        version_scan = nmap1.nmap_ping_scan(host_entry.get())
        with open('Ping_Scan.json', 'w') as file:
            file.write(json.dumps(version_scan))
        success_label = Label(root, text='Scan Completed!')
        success_label.grid_forget()
        success_label.grid(row=2, column=0)

    elif scan_type == '':
        fail_label = Label(root, text='Scan Failed :( ')
        fail_label.grid(row=2, column=0)


submit = Button(root, text='Submit', command=scan)

host_label.grid(row=0, column=0)
host_entry.grid(row=0, column=1)
scan_label.grid(row=1, column=0)
scan_select.grid(row=1, column=1)
submit.grid(row=0, column=2)
mainloop()
