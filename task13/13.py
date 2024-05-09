from ipaddress import ip_network

net = ip_network('95.112.224.0/255.255.255.128', False)
k = 0
for ad in net:
    temp = f'{int(ad):0>32b}'[-8:]
    if temp == temp[::-1]:
        k += 1
print(k)