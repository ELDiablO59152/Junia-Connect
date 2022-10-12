import requests

r = requests.get('http://www.gstatic.com/generate_204')  # Get the magic number from the firewall
print(r.text)

if r.text != '':
    try: magic = r.text.split('?')[1].split('"')[0]  # Parse the magic number from the request
    except: print("Impossible to get magic number")
    else: print("Magic number:", magic)

    r = requests.get('https://wifi-students.junia.com:1003/fgtauth?' + magic)  # Activation of the magic number
    print(r.text)

    mail = "Put your mail address here in the .py"
    password = "Put your password here in the .py"

    # Authentication request
    requests.post('https://wifi-students.junia.com:1003/', data={'4Tredir': 'http://www.gstatic.com/generate_204', 'magic': magic, 'username': mail, 'password': password})

    r = requests.get('http://www.gstatic.com/generate_204')  # Make sure the firewall is satisfied
    print(r.text)

    if r.text == '':  # Blank answer means a successful authentication
        print("Success !")
    else:
        input("Authentication failed")
            
else: print("Error, already connected or impossible to reach firewall")
