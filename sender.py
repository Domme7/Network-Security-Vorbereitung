import socket
import base64

# lese Datei 
with open ("robotergesetze.txt", "r", encoding="utf-8") as file:
    data = file.read()

# kodiere Daten
encoded_data = base64.b64encode(data.encode())

# erstelle TCP-Socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('192.168.0.104', 65432)) # verbindet mit Programm B (Empfänger)
    s.sendall(encoded_data) # senden der Daten
    print("Daten gesendet.")
    