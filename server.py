import socket
import threading

HOST ='127.0.0.1'
PORT=9090

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
clients=[]
nicknames=[]

#broadcast
def broadcast(message):
    for client in clients:
        client.send(message)

# handle  
def handle(client):
    while True:
        try:
            message=client.recv(1024)
            print(f"{nicknames[clients.index(client)]}says{message}")
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            broadcast("{} left the chat".format(nickname).encode('utf-8'))
            nicknames.remove(nickname)
            break

# recieve

def recieve():
    while True:
        client,addr=server.accept() #it will accept the connection andn return the client and address 
        print(f"connected with {str(addr)}")
        client.send("NICK".encode('utf-8'))
        nickname=client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        print("Nickname of the client is {}".format(nickname))
        broadcast("{} joined the chat\n".format(nickname).encode('utf-8')) 
        client.send("Connected to the server".encode('utf-8'))
        thread=threading.Thread(target=handle,args=(client,))
        thread.start()

print("Server is listening...")
recieve()

      