import base64

username = "string"
password = "string"
credentials = f"{username}:{password}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()
print(encoded_credentials)