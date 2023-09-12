import smtplib
import ssl
from email.message import EmailMessage

def send_email(sender_email, receiver_email, password, subject, body):
    try:
        # Create an EmailMessage object
        message = EmailMessage()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # Create an HTML message
        html = f"""
        <html>
            <body>
                <h1>{subject}</h1>
                <p>{body}</p>
            </body>
        </html>
        """
        message.add_alternative(html, subtype="html")

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Connect to Gmail's SMTP server using SSL
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            # Login to your Gmail account using the provided password
            server.login(sender_email, password)

            # Send the email
            server.sendmail(sender_email, receiver_email, message.as_string())

        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    sender_email = "dragonfever11@gmail.com" # Your Gmail address
    receiver_email = "dragonfever11@gmail.com"   # Recipient's email address
    password = "ffagzehafgqegbgc"  # Your app-specific password
    subject = "Email From Python"
    body = "This is a test email from Python!"

    send_email(sender_email, receiver_email, password, subject, body)
