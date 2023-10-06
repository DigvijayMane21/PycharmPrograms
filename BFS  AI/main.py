def validate_ip(s):
    # check number of periods
    if s.count('.') != 3:
        return 'Invalid Ip address'

    ip_list = list(map(str, s.split('.')))

    # check range of each number between periods  
    for element in ip_list:
        if int(element) < 0 or int(element) > 255 or (element[0] == '0' and len(element) != 1):
            return 'Invalid IP address'

    return 'Valid IP address'

ip=input("Enter an IP: ")
print(validate_ip(ip))

Enter an IP: 192.168.0.1
Valid IP address
