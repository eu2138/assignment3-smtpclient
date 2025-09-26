from socket import *
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging


def smtp_client(port=1025, mailserver='127.0.0.1'):
    message = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start

    
    file_content = ""
    file_receiver = ""

    try:
        with open('.smtppassword', 'r') as file:
            # The 'r' mode means read-only.
            file_content = file.read()
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        with open('.receiveremailaccount', 'r') as file:
            # The 'r' mode means read-only.
            file_receiver = file.read()
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587# For starttls
        sender_email = "eu2138@nyu.edu"
        password = file_content 

        # Create a secure SSL context
        # context = ssl.create_default_context()

        # Try to log in to server and send email

        print("initializing server variable\n")

        server = smtplib.SMTP(smtp_server,smtp_port,timeout=30)
        #print("server")
        # Create a secure SSL context
        #context = ssl.create_default_context()
        #server.starttls(context=context) # Secure the connection
        server.starttls() # Secure the connection
        #server.helo() # Can be omitted
        print("pre-login")
        server.login(sender_email, password)
        server.helo() # Can be omitted
        print("post-login")
        server.sendmail(sender_email, file_receiver, "Hello World!")
        print("sent mail successful")
        server.quit()

        print("break")
        # recv = clientSocket.recv(1024).decode()
        # print(recv) #You can use these print statement to validate return codes from the server.
        #if recv[:3] != '220':
        #    print('220 reply not received from server.')

        # Send HELO command and print server response.

        msg = "\r\n My message"
        endmsg = "\r\n.\r\n"
        print("break")

        # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

        # Create socket called clientSocket and establish a TCP connection with mailserver and port

        # Fill in start
        # ===============================================
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind((mailserver, port))
        serverSocket.listen()
        clientSocket, addr = serverSocket.accept()#Fill in start -are you accepting connections?     #Fill in end
        # ===============================================

        # Fill in end


        heloCommand = 'HELO Alice\r\n'
        clientSocket.send(heloCommand.encode())
        print("break")
        recv1 = clientSocket.recv(1024).decode()
        print("break")
        #print(recv1) 
        #if recv1[:3] != '250':
        #    print('250 reply not received from server.')

        #with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        #    server.login("eu2138@nyu.edu", password)

        # TODO: Send email here
        # Send MAIL FROM command and handle server response.
        # Fill in start

        
        # Fill in end

        # Send RCPT TO command and handle server response.
        # Fill in start
        # Fill in end

        # Send DATA command and handle server response.
        # Fill in start
        # Fill in end

        # Send message data.
        # Fill in start
        # Fill in end

        # Message ends with a single period, send message end and handle server response.
        # Fill in start
        # Fill in end




    except Exception as e:
        # Print any error messages to stdout
        logging.basicConfig(level=logging.ERROR)  # Set logging level
        logging.exception("An error occurred:" + str(e))
    
        # Send QUIT command and handle server response.
        # Fill in start
    finally:
        print("Closing sockets\n")
        clientSocket.close()
        serverSocket.close()
        # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
