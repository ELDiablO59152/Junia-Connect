import sys
import requests
from getpass import getpass
from subprocess import check_output


def VerifWiFi():
    debug = False
    for arguments in sys.argv:
        if arguments == "debug": debug = True
    
    SSID = check_output(["powershell", "-Command", "(get-netconnectionProfile).Name"], shell=False).strip()
    if b'JUNIA_STUDENTS' in SSID: JuniaConnect(debug)
    elif debug:
        try: SSID = SSID.decode()
        except: pass
        print("Wrong WiFi:", SSID)
        input("Press Enter to exit")
    else: print("Wrong WiFi:", SSID)

    return


def JuniaConnect(debug):
    mail = ""
    password = ""
    for arguments in sys.argv:
        if arguments.split('=')[0] == "mail": mail = arguments.split('=')[1]
        elif arguments.split('=')[0] == "password": password = arguments.split('=')[1]

    try: r = requests.get('http://www.gstatic.com/generate_204')  # Get the magic number from the firewall
    except: print("Error while reaching internet, check your connection")
    if debug: print(r.text)

    if r.text != '':
        try: magic = r.text.split('?')[1].split('"')[0]  # Parse the magic number from the request
        except: print("Impossible to get magic number")
        else: print("Magic number:", magic)

        r = requests.get('https://wifi-students.junia.com:1003/fgtauth?' + magic)  # Activation of the magic number
        if debug: print(r.text)

        notconnected = True

        while notconnected :
            if not mail: mail = input("Mail Address: ")
            print ("Account:", mail)
            if not password: password = getpass()

            # Authentication request
            requests.post('https://wifi-students.junia.com:1003/', data={'4Tredir': 'http://www.gstatic.com/generate_204', 'magic': magic, 'username': mail, 'password': password})

            r = requests.get('http://www.gstatic.com/generate_204')  # Make sure the firewall is satisfied
            if debug: print(r.text)

            if r.text == '':  # Blank answer means a successful authentication
                notconnected = False
                print("Success !")
            else:
                mail = ""
                password = ""
                input("Authentication failed")

    else: input("Error, already connected or impossible to reach firewall\nPress Enter to exit")
    return


print("Junia-Connect v1.2")
VerifWiFi()
