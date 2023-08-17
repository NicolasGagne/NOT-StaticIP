"""
Main file for the program
"""

from urllib import request, parse
import requests
from private import private
import json
import datetime, time

headers = {
    'accept': private.API_accept,
    'API-Key': private.API_KEY,
    'Content-Type': private.API_Content_Type,
}

def get_my_IP():
    """

    :return: Sting containg the IP adress "XXX.XXX.XXX.XXX"
    """
    return request.urlopen('https://ident.me').read().decode('utf8')

def check_ip():
    """

    :return: LIst of Sting containg the IP adress in account of DDNS ["XXX.XXX.XXX.XXX",]
    """
    list_IP = []

    response = requests.get(private.API_DNS_URL + 'dns', headers=headers)

    # Check if response was successful
    if response.status_code == 200:

        # Do the routine for each domain under that account
        for dom_dict in response.json()['domains']:
            list_IP.append(dom_dict['ipv4Address'])

        return list_IP

    else:
        print('Login error, check api Key')

        return None





def update_my_IP(my_IP):
    """
    
    :param my_IP: String value of my cureent IP
    :return: True if OK  or False if error
    """

    response = requests.get(private.API_DNS_URL + 'dns', headers=headers)

    # Check if response was successful
    if response.status_code == 200:

        # Do the routine for each domain under that account
        for dom_dict in response.json()['domains']:
            new_dom_dict = {}

            # Modifie the list for return it back to the API
            for key in dom_dict:
                if key in private.API_key_list:
                    new_dom_dict[key] = dom_dict[key]

            # Modified the IPv4 with the new IP
            new_dom_dict['ipv4Address'] = my_IP
            json_dom = json.dumps(new_dom_dict)

            # Post to update the IP
            response = requests.post(private.API_DNS_URL + 'dns/' + str(dom_dict["id"]), headers=headers, data=json_dom)

            # Check if the above post was successful.
            if response.status_code == 200:
                print('Address with <<' + dom_dict['name'] + ">> has been update with your current IP" + " New IP: " + my_IP)
            else:
                print('ERROR: Address with <<' + dom_dict['name'] + ">> Something wrong...")

            return True

    else:
        print('Login error, check api Key')
        return False




def main():
    """
    Runnign the all program.
    :return: None
    """

    while True:
        list_check_ip = check_ip()
        my_IP = get_my_IP()

        if list_check_ip == None:
            break

        if len(set(list_check_ip)) == 1 and list_check_ip[0] != my_IP:

            if update_my_IP(my_IP):
                p = 'IP Update completed at:' + datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S') + " New IP: " + my_IP
                print(p)

            else:
                p = "Error append at: " + datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
                print(p)
                

        elif len(list_check_ip) == 1 or list_check_ip[0] == my_IP:
            p = 'IP do not need to be change at:' + datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S') + " IP: " + my_IP
            print(p)
            
        with open("LOG.txt", "a+") as f:
            f.write(p)
            f.write('\n')

        time.sleep(600)




if __name__ == '__main__':
    print("Program Not Static IP Start")
    main()
    print('End without error')
