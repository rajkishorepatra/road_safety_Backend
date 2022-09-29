import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_mail(name,rec_email):
    mail_content = f'''Hello {name},
    Thank you for taking the Road Safety Pledge.
    Please find your certificate below.'''

    sender_address = 'ece.20beca70@silicon.ac.in'
    sender_pass = 'raja0642'
    receiver_address = rec_email

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Pledge Certificate'
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = f'certificates/{name}_{rec_email}_certificate.pdf'
    with open(attach_file_name,'rb') as f:
        attachment = MIMEApplication(f.read(), Name=basename(attach_file_name))
        attachment['Content-Disposition'] = 'attachment; attach_file_name="{}"'.format(basename(attach_file_name))
    message.attach(attachment)
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    session.send_message(message, sender_address, receiver_address)
    session.quit()
    print('Mail Sent')