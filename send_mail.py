from email import message
import smtplib
# allows us to send text in HTML emails
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    username = '9eb8ba1fc1e0b8'
    password = 'd32a5c69fc36d2'
    message = f'<h3>New Feedback Submission </h3> <ol><li>Customer:{customer}</li><li>Dealer:{dealer}</li><li>Rating:{rating}</li><li>Comments:{comments}</ li></ol>'


    sender_email = 'harshan.gandamalla@gmail.com'
    receiver_email = 'receiver@gmail.com'
    my_message = MIMEText(message, 'html')
    my_message['Subject'] = 'LEXUS FEEDBACK'
    my_message['From'] = sender_email
    my_message['To'] = receiver_email

    # How to send the mail
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, my_message.as_string())
