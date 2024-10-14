import socket
import base64

# TCP-Socket zum lauschen
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', 65432)) # Lauschen auf Port 65432
    s.listen()
    print("Warten auf Verbindung...")

    conn, addr = s.accept() # Verbindung akzeptieren 
    with conn:
        print(f"Verbunden mit {addr}")
        data = conn.recv(1024) # Empfangen der Daten 
        decoded_data = base64.b64decode(data).decode('utf-8') # Dekodiere Daten
        print("Empfangene Daten:")
        print(decoded_data)