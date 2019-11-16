import smtplib

def send_email(name, email_id, type):
    """
    send email to email_id 
    input: name of user, emailid, type (of message eg: signup)
    output: sends email
    """
    sender_email = your_mail_id #source from mail will send
    message = ""
    if(type == "signup"):
        message = f"""
        Welcome {name},

        Test sending email using python smtp. Hope you will get better experience with us.

        Regards,
        **********.
        """
    else: message = """
            other email
            """
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login(api_regesterd_mail(gmail),password)
    mail.sendmail(sender_email, email_id, message)
    mail.close()   

