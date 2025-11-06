import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = ""
receiver_email = "receiver_email@gmail.com"
password = "your_app_password"  

subject = "Test Email from Python"
body = "Hello! This is a test email sent using Python. 😊"


msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls() 
    server.login(sender_email, password)
    server.send_message(msg)

print("✅ Email sent successfully!")
