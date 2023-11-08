import socket
import json
from googletrans import Translator
# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.241.9" # Host IP address
port = 8000 # Port number
server_socket.bind((host, port))
server_socket.listen(5)
print(f"Translation service is up and running on {host}:{port}...")
while True:# Accept incoming client connections
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr} has been established.")
    # Receive data from the client
    data = client_socket.recv(1024).decode("utf-8")
    if data:
        # Load JSON data
        data = json.loads(data)
        text = data.get("text", "")
        target_language = data.get("target_language", "en")
        # Translate text using machine translation API
        translator = Translator()
        translated_text = translator.translate(text, 
        dest=target_language).text
        # Prepare response data as JSON
        response_data = {"translated_text": translated_text}
        response = json.dumps(response_data).encode("utf-8")
        # Send translated text back to the client
        client_socket.send(response)
    else:
        # Send error message if no data received
        error_response = json.dumps({"error": "No data received"}).encode("utf-8")
        client_socket.send(error_response)
        # Close client socket
    client_socket.close()