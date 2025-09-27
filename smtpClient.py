from socket import *
import logging

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    try:
        # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

        # Create socket called clientSocket and establish a TCP connection with mailserver and port

        # Fill in start
        
        serverAddress = (mailserver, port)
        clientSocket = socket(AF_INET, SOCK_STREAM)

        #Fill in start

        clientSocket.connect(serverAddress)

        # Fill in end

        recv = clientSocket.recv(1024).decode()
        # print("Receive: " + recv[:3] + " : End\n") #You can use these print statement to validate return codes from the server.
        #print(recv)
        #if recv[:3] != '220':
        #    print('220 reply not received from server.')  

        heloCommand = 'HELO Alice\r\n'
        clientSocket.send(heloCommand.encode())
        recv1 = clientSocket.recv(1024).decode()

        #print(recv1) 
        #if recv1[:3] != '250':
        #    print('250 reply not received from server.')

        # Send MAIL FROM command and handle server response.
        # Fill in start

        # server.send("MAIL FROM".encode())
        clientSocket.send("MAIL FROM".encode())
        recv2 = clientSocket.recv(1024).decode()
        
        # Fill in end

        # Send RCPT TO command and handle clientSocket response.
        # Fill in start

        clientSocket.send("RCPT TO".encode())
        recv3 = clientSocket.recv(1024).decode()

        # Fill in end

        # Send DATA command and handle clientSocket response.
        # Fill in start

        clientSocket.send("DATA".encode())

        # Fill in end

        # Send message data.
        # Fill in start

        clientSocket.send(msg.encode())

        # Fill in end

        # Message ends with a single period, send message end and handle clientSocket response.
        # Fill in start
        
        clientSocket.send(endmsg.encode())
        recv4 = clientSocket.recv(1024).decode()

        # Fill in end

        # Send QUIT command and handle server response.
        # Fill in start

        clientSocket.send("QUIT".encode())
        recv5 = clientSocket.recv(1024).decode()

        # Fill in end


    except Exception as e:
        # Print any error messages to stdout
        logging.basicConfig(level=logging.ERROR)  # Set logging level
        logging.exception("An error occurred:" + str(e))
    
    finally:
        clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
    #smtp_client(587, 'smtp.gmail.com')
