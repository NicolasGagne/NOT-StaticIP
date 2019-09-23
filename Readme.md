The gold is to overcome the problem of not having a static by using a DDNS provider and automatic update the IP with your current one.

I use the following DDNS privider: https://www.dynu.com/en-US/ 



How to:

- Setup an account on the dynu.com site and make sure it working properly.
(Note: This will update all the IP for all the domain under that account.)
- Get your own API Key the and put it in the file private.py; Documentation at: https://www.dynu.com/Resources/API
- Run on the same network as the server on a seprate console, the program will keep checking the IP each 10 min.

Coming soon:

- Executable version for other language