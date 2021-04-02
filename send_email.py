import smtplib, ssl
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Send_email:
    def send_mail(self):
        """
        input variables
        receiver_mail string:
        email to be given

        subject string:
        subject of the mail to be given

        body string:
        body of the mail to be given

        Purpose of the class:
        To send email to the specified recipient according the input of email, body and subject given.

        """
        receiver_mail = input("Recipient?")
        subject = input("Subject?")
        body = input("Body?")
        try:
            sender_email = "kasmithar3@gmail.com"
            password = "21July@1998"
            receiver_email = receiver_mail

            message = MIMEMultipart("alternative")
            message["Subject"] = subject
            message["From"] = sender_email
            message["To"] = receiver_email

            # Turn these into plain/html MIMEText objects
            part1 = MIMEText(body, "html")
            # The email client will try to render the last part first
            message.attach(part1)

            # Create secure connection with server and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())

            "To clear Garbage collection"
            del part1
            del context
            del receiver_mail
            del subject
            del body
            del sender_email
            del password
            print("Email sent!")
        except smtplib.SMTPRecipientsRefused:
            print("Kindly enter a valid recipient or email id")
        except Exception as e:
            traceback.print_exc()
            print(e)

email = Send_email()
email.send_mail()