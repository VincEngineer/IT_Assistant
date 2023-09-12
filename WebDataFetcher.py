import requests
import json

'''
It will fetch data from your Hack the box account, it will also assume you spawned the pwnbox machine already.
we use this class to feed the ToolingPanel.py
'''


class HTBMachineStatus:
    def __init__(self, email, password):
        self.session = requests.Session()
        self.password = password
        self.email = email
        self.vnc_password = None
        self.access_token = None
        self.user_name = None
        self.hostname = None
        self.headers = None

    def login(self):
        login_url = 'https://www.hackthebox.com/api/v4/login'
        payload = {
            "email": self.email,
            "password": self.password
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json',
            'Origin': 'https://app.hackthebox.com',
            'Referer': 'https://app.hackthebox.com/',
        }
        response = self.session.post(login_url, json=payload, headers=self.headers)

        # Check if the login request was successful
        if response.status_code == 200:
            response_data = json.loads(response.text)
            self.access_token = response_data.get('message', {}).get('access_token')
            return True
        else:
            return False

    def fetch_machine_status(self):
        if self.access_token:
            pwnbox_status_url = 'https://www.hackthebox.com/api/v4/pwnbox/status'
            # Update headers for authenticated GET request
            self.headers['Authorization'] = f'Bearer {self.access_token}'

            # Perform the GET request to get Pwnbox status

            pwnbox_response = self.session.get(pwnbox_status_url, headers=self.headers)

            # Check if the GET request was successful (VIEW INSTANCE DETAILS)
            if pwnbox_response.status_code == 200:
                pwnbox_data = json.loads(pwnbox_response.text)

                # Extract the desired information
                self.hostname = pwnbox_data.get('hostname')
                self.user_name = pwnbox_data.get('user_name')
                self.vnc_password = pwnbox_data.get('vnc_password')

                print(f"Hostname: {self.hostname}")
                print(f"Username: {self.user_name}")
                print(f"VNC Password: {self.vnc_password}")
