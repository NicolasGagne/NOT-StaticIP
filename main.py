"""
Main file for the program
"""

import urllib.request

def get_my_IP():
    """

    :return: Sting containg the IP adress "XXX.XXX.XXX.XXX"
    """
    return urllib.request.urlopen('https://ident.me').read().decode('utf8')



def main():
    """
    Runnign the all program.
    :return: None
    """
    my_external_IP = get_my_IP()




if __name__ == '__main__':
    print("Program Not Static IP Start")
    main()