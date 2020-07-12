# Author Andy Fang
# -*- coding:utf-8 -*-
import sys
import threading
import IPy
import nmap
import json
from concurrent.futures import  ThreadPoolExecutor


def getiplist(ip_range):
    start_ip = ip_range.split('-')[0]
    end_ip = ip_range.split('-')[1]
    ipPool = [IPy.intToIp(ip, 4) for ip in range(IPy.IP(start_ip).int(), IPy.IP(end_ip).int() + 1)]
    return  ipPool

def checkhostalive(ip_addr):
    nm = nmap.PortScanner()
    try:
        results = nm.scan(hosts=ip_addr, arguments='-sn')
        for res in  results['scan'].values():
            if res['status']['state'] == 'up':
                print(f'host: {ip_addr} is alive')
    except Exception as e:
        print(e)

def checkportalive(ip_addr, port,openport_list):
    nm = nmap.PortScanner()
    try:
        results = nm.scan(hosts=ip_addr, ports=str(port) )
        res = results['scan'][ip_addr]['tcp'][port]['state']
        if res == 'open':
            open_port_list.append(port)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    argv = sys.argv[1:]
    value = argv[1::2]
    key = argv[0::2]
    parameter = dict(zip(key, value))
    if parameter['-f'] == 'ping':
        iplist = getiplist(parameter['-ip'])
        with ThreadPoolExecutor(int(parameter['-n'])) as executor01:
                executor01.map(checkhostalive,iplist)
    elif parameter['-f'] == 'tcp':
        open_port_list = []
        with ThreadPoolExecutor(int(parameter['-n'])) as executor02:
            for port in range(1, 100):
                executor02.submit(checkportalive, parameter['-ip'], port, open_port_list)
        open_port_dict = {
            'ip': parameter['-ip'],
            'ports': open_port_list
        }
        with open(parameter['-w'], 'w', encoding='utf-8')as f:
            f.write(json.dumps(open_port_dict))
    else:
        print('请输入正确的命令格式!!!')
