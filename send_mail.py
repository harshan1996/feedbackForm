from email.message import EmailMessage
import smtplib
import ssl

def send_mail(customer, dealer, rating, comments):

    email_sender = 'harshan.gandamalla@gmail.com'
    email_password = ''
    email_receiver = 'receiver@gmail.com'

    # Subject and body of the email
    subject = 'Feedback Submission'
    body = f"""
    Customer: {customer}
    Dealer: {dealer}
    Rating: {rating}
    Comments: {comments}
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
