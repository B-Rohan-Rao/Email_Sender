import smtplib

# Set up the email details
sender = 'Sender@gmail.com'
recipient = 'recipient@gmail.com'
subject = input("Enter the subject: ")
body = input("Enter the body: ")

# Create the email message
message = f'Subject: {subject}\n\n{body}'

try:
    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    # Login to the SMTP server
    server.login(sender, 'cptg lvrt nfwg whus')     #<<<Enter the app key as second parameter as a string
        
    # Send the email
    server.sendmail(sender, recipient, message)
    
    print('Message sent successfully!')
except smtplib.SMTPException as e:
    print(f'Error sending email: {e}')
finally:
    # Close the SMTP server connection
    server.quit()
