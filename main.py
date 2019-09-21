"""
Main file for the program
"""

from urllib import request, parse
import requests
from private import private
import json



def get_my_IP():
    """

    :return: Sting containg the IP adress "XXX.XXX.XXX.XXX"
    """
    return request.urlopen('https://ident.me').read().decode('utf8')


def update_my_IP(my_IP):
    """
    
    :param my_IP: String value of my cureent IP
    :return: None
    """

    headers = {
        'accept': private.API_accept,
        'API-Key': private.API_KEY,
        'Content-Type': private.API_Content_Type,
    }

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
                print('Address with <<' + dom_dict['name'] + ">> has been update with your current IP")
            else:
                print('ERROR: Address with <<' + dom_dict['name'] + ">> Something wrong...")

    else:
            print('Login error, check api Key')


def main():
    """
    Runnign the all program.
    :return: None
    """
    update_my_IP(get_my_IP())




if __name__ == '__main__':
    print("Program Not Static IP Start")
    main()
    print('End without error')