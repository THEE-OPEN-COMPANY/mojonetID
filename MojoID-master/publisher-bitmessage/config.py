import os

site_address = "yoursiteaddress"
site_privatekey = "yoursiteprivatekey"
# ~/.config/PyBitmessage/keys.dat (apiusername = user, apipassword = pass)
bitmessage_url = "http://apiusername:apipassword@localhost:8442/"

mojonet_dir = "/home/mojonet/"
logfile = os.path.dirname(os.path.realpath(__file__))+"/bitmessage.log"

# To install add this lint to ~/.config/PyBitmessage/keys.dat [bitmessagesettings] section:
# apinotifypath = /home/mojonet/bitmessage-adder/bitmessage.py
