import socket
import json
# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.241.9" # Host IP address
port = 8000 # Port number
# Connect to the server
client_socket.connect((host, port))
# Input text to be translated
text = input("Enter text to be translated :" )
target_language = input("Enter target language (default is 'en') :" )
# Prepare data as JSON
data = {"text":text, "target_language": target_language}
data = json.dumps(data).encode("utf-8")
# Send data to the server
client_socket.send(data)
# Receive translated text from the server
response = client_socket.recv(1024).decode("utf-8")
if response:
    # Load JSON response
    response_data = json.loads(response)
    translated_text = response_data.get("translated_text", "")
    print("Translated Text:", translated_text)
else:
    print("Error No response received from the server.")
    # Close client socket
    client_socket.close()