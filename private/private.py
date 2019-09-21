"""
All private information for the login and other


Replace None with your private information
"""


"""
DDNS PROVIDER
I use https://www.dynu.com 
You have to modified the code fi you use another proveder
"""

API_KEY = "PUT YOU API KEY from: https://www.dynu.com"
API_DNS_URL = "https://api.dynu.com/v2/"
API_accept = "application/json"
API_Content_Type = "application/json"

# list the key that will be needed for a post
API_key_list =[
    "name",
    "group",
    "ipv4Address",
    "ipv6Address",
    "ttl",
    "ipv4",
    "ipv6",
    "ipv4WildcardAlias",
    "ipv6WildcardAlias",
    "allowZoneTransfer",
    "dnssec"
]