from socket import *
# import smtplib, ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.message import EmailMessage
import logging

smtp_server = 'smtp.gmail.com'
smtp_port = 587 # For starttls

# smtp_server = "127.0.0.1"
# smtp_port = 1025 # For starttls

def smtp_client(port=1025, mailserver='127.0.0.1'):
    message = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start

    PASSWORD = ""
    SENDER_EMAIL = ""
    RECIPIENT_EMAIL = ""

    # This is a mess but we can clean it up later if necessary
    try:
        with open('.smtppassword', 'r') as file:
            PASSWORD = file.read()
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        with open('.senderemailaccount', 'r') as file:
            SENDER_EMAIL = file.read()
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        with open('.receiveremailaccount', 'r') as file:
            RECIPIENT_EMAIL = file.read()
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:

        # --- Email Content ---
#        msg = EmailMessage()
#        msg.set_content("This is a test email sent from a localhost Python script connecting to Gmail's SMTP server.")
#        msg['Subject'] = 'Test Email from Localhost Client'
#        msg['From'] = SENDER_EMAIL
#        msg['To'] = RECIPIENT_EMAIL 

        # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

        # Create socket called clientSocket and establish a TCP connection with mailserver and port

        # Fill in start
        
        # Instantiate socket called clientSocket

        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((mailserver, port))

        # Fill in end

        recv = clientSocket.recv(1024).decode()
        # print("Receive: " + recv[:3] + " : End\n") #You can use these print statement to validate return codes from the server.
        print(recv)
        if recv[:3] != '220':
            print('220 reply not received from server.')  

        heloCommand = 'HELO Alice\r\n'
        clientSocket.send(heloCommand.encode())
        recv1 = clientSocket.recv(1024).decode()

        clientSocket.send("hello".encode())

        print(recv1) 
        if recv1[:3] != '250':
            print('250 reply not received from server.')

        # TODO: Send email here
        # Send MAIL FROM command and handle server response.
        # Fill in start

        # server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, recv + "\n" + recv1)
        
        # Fill in end

        # Send RCPT TO command and handle server response.
        # Fill in start

        # server.sendto("RCPT TO", mailserver)

        # Fill in end

        # Send DATA command and handle server response.
        # Fill in start

        #server.send("DATA")

        # Fill in end

        # Send message data.
        # Fill in start

        #ancillary_data = [
        #    (socket.SOL_SOCKET, socket.SCM_RIGHTS, fd_to_send_bytes)
        #]

        # server.sendmsg("message")

        # Fill in end

        # Message ends with a single period, send message end and handle server response.
        # Fill in start
        
        # server.sendall("message.")

        # Fill in end


    except Exception as e:
        # Print any error messages to stdout
        logging.basicConfig(level=logging.ERROR)  # Set logging level
        logging.exception("An error occurred:" + str(e))
    
        # Send QUIT command and handle server response.
        # Fill in start
    finally:
        clientSocket.close()
        # Fill in end


if __name__ == '__main__':
    # smtp_client(1025, '127.0.0.1')
    smtp_client(smtp_port, smtp_server)
