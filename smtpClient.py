from socket import *
# import smtplib, ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.message import EmailMessage
import logging

# smtp_server = "127.0.0.1"
# smtp_port = 1025 # For starttls

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start

    # PASSWORD = ""
    # SENDER_EMAIL = ""
    # RECIPIENT_EMAIL = ""

    try:
        # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

        # Create socket called clientSocket and establish a TCP connection with mailserver and port

        # Fill in start
        
        # Instantiate socket called clientSocket

        serverAddress = (mailserver, port)

        #print("Ok")

        clientSocket = socket(AF_INET, SOCK_STREAM)

        #print("Ok")

        #Prepare a server socket
        #clientSocket.bind(serverAddress)

        #Fill in start
        #clientSocket.listen(1)

        clientSocket.connect(serverAddress)

        #print("Ok")

        # Create a secure SSL context
        # context = ssl.create_default_context()

        # print("server: " + mailserver + " port: " + str(port))
        #server = smtplib.SMTP(mailserver,port)
        # print("ok")
        #server.helo() # Can be omitted
        # server.starttls() # Secure the connection
        # print("ok")
        # server.helo() # Can be omitted
        # server.login(SENDER_EMAIL, PASSWORD)

        # TODO: Send email here
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

        # TODO: Send email here
        # Send MAIL FROM command and handle server response.
        # Fill in start

        # server.send("MAIL FROM".encode())
        clientSocket.send("MAIL FROM".encode())
        
        # Fill in end

        # Send RCPT TO command and handle clientSocket response.
        # Fill in start

        clientSocket.send("RCPT TO".encode())

        # Fill in en

        # Send DATA command and handle clientSocket response.
        # Fill in start

        clientSocket.send("DATA".encode())

        # Fill in end

        # Send message data.
        # Fill in start

        #ancillary_data = [
        #    (socket.SOL_SOCKET, socket.SCM_RIGHTS, fd_to_send_bytes)
        #]

        clientSocket.send(msg.encode())

        # Fill in end

        # Message ends with a single period, send message end and handle clientSocket response.
        # Fill in start
        
        clientSocket.send(endmsg.encode())

        # Fill in end

        # Send QUIT command and handle server response.
        # Fill in start

        clientSocket.send("QUIT".encode())

        # Fill in end


    except Exception as e:
        # Print any error messages to stdout
        logging.basicConfig(level=logging.ERROR)  # Set logging level
        logging.exception("An error occurred:" + str(e))
    
        # Send QUIT command and handle server response.
        # Fill in start
    finally:
        clientSocket.close()
        # server.quit()
        # Fill in end


if __name__ == '__main__':
    #smtp_client(1025, '127.0.0.1')
    #smtp_server = 'smtp.gmail.com'
    #smtp_port = 587 # For starttls
    smtp_client(587, 'smtp.gmail.com')
