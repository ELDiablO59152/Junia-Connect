import sys
import requests
from getpass import getpass
from subprocess import check_output


def VerifWiFi():
    SSID = check_output(["powershell", "-Command", "(get-netconnectionProfile).Name"], shell=False).strip()
    if SSID == b'JUNIA_STUDENTS':
        JuniaConnect()
    else:
        print("Wrong WiFi:", SSID.decode())
    return


def JuniaConnect():
    mail = ""
    password = ""
    debug = False
    for arguments in sys.argv:
        if arguments.split('=')[0] == "mail": mail = arguments.split('=')[1]
        elif arguments.split('=')[0] == "password": password = arguments.split('=')[1]
        elif arguments == "debug": debug = True

    r = requests.get('http://www.gstatic.com/generate_204')  # Get the magic number from the firewall
    if debug: print(r.text)

    if r.text != '':
        try: magic = r.text.split('?')[1].split('"')[0]  # Parse the magic number from the request
        except: print("Impossible to get magic number")
        else: print("Magic number:", magic)

        r = requests.get('https://wifi-students.junia.com:1003/fgtauth?' + magic)  # Activation of the magic number
        if debug: print(r.text)

        notconnected = True

        while notconnected :
            mail = input("Mail Address: ")
            print ("Account:", mail)
            password = getpass()

            # Authentication request
            requests.post('https://wifi-students.junia.com:1003/', data={'4Tredir': 'http://www.gstatic.com/generate_204', 'magic': magic, 'username': mail, 'password': password})

            r = requests.get('http://www.gstatic.com/generate_204')  # Make sure the firewall is satisfied
            if debug: print(r.text)

            if r.text == '':  # Blank answer means a successful authentication
                notconnected = False
                print("Success !")
            else:
                input("Authentication failed")

    else: input("Error, already connected or impossible to reach firewall")
    return


VerifWiFi()
