import smtplib
import ssl

# Load credentials
with open('./coolpc_checker/credentials.txt') as fh:
    email, password = fh.read().split()


# https://realpython.com/python-send-email
smtp_server = 'smtp.gmail.com'
port = 587  # For starttls

context = ssl.create_default_context()
msg = '''Subject: test

hello world
'''

# Log in and send email
try:
    with smtplib.SMTP(smtp_server, port, timeout=5) as server:
        server.starttls(context=context)
        server.login(email, password)

        # Send email
        server.sendmail(
            from_addr=email,
            to_addrs=email,  # Send to self
            msg=msg
        )
except Exception as e:
    print(e)
