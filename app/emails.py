from time import time
from celery import shared_task
from mailersend import emails



mailersend_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNTk4Y2E1YWY3Y2I5MGI3NzI1YTA5MDAzMDNlNjA3MDg3ZjQxNmRkZDU2NmQwNTIyYTA0NDYzOTE2NDA1YWFkYjExNWY3M2QzYTU2NDEzM2IiLCJpYXQiOjE2NDcxMDIyNjEuMjgxMDYsIm5iZiI6MTY0NzEwMjI2MS4yODEwNjQsImV4cCI6NDgwMjc3NTg2MS4yNzc4LCJzdWIiOiIyMjg1MSIsInNjb3BlcyI6WyJlbWFpbF9mdWxsIiwiZG9tYWluc19mdWxsIiwiYWN0aXZpdHlfZnVsbCIsImFuYWx5dGljc19mdWxsIiwidG9rZW5zX2Z1bGwiLCJ3ZWJob29rc19mdWxsIiwidGVtcGxhdGVzX2Z1bGwiLCJzdXBwcmVzc2lvbnNfZnVsbCJdfQ.oJEFbGoLaCUPhyL17Tn-Kb2lPrw3HQWpJjODavU7d4s-NbJrg1Gs2o9d9gcnCGxOu-Js1KiOCofXh2iZe6w_6LYU2fNxGewjlD47FXA-ckseuJXiOaX1Y7yam5zQ7_UDFDppon06aLPZsh0fFakSyBkC6UBdk08VBrEE47tjwySXNryOQrBVosA1r-SIrYNc_vtGjEek-IVasFY65sslD7ZC--QgBsJuW6AuSg2WZjMUmaziBOjW6mKk0OChqOCfTxqUQC_JNC4f4BCcLd6qcd9w3i-yKSErb4fVhv4rIML2MN6AzsDFbDhc8LbqNGOP-7ctY2ahOVlyMVXBVG00KSyt7Artbdj1o5VAeeVoMqClA4kWZtoJFUW1Ju8HacGMDkQJn_2dFuyfKY35ft5C17RNRRg56qSQzPcLqSVrj1RcXRfETIeiATanG9hHyC7OqecsolAINCEqRTzeLNnchWA05CLUHh8FlMiDtPMeyjo8FeIvlczFO-xsAeBQLk67xLaDxlRQMQQVKzlTTLFuF-5aUaPkB_UHTqozfPQEU82HRWFQJs2OmODZ5vUXe_GOhcac248XCgxMX8mr-djKPk4EmCIZrjkAp2ZrNScyZw83sKYPhw84A5TYqxmIA7FOkRjTJ1d_Bt3KZeXkwRKAa-oioTHWWCvKV5t0vu4c_U8"

@shared_task(name="send_email_with_mailersend")
def send_email(email: str, text: str, subject: str) -> None:
    mailer = emails.NewEmail()

# define an empty dict to populate with mail values
    mail_body = {}

    mail_from = {
        "name": "SAMSANTECH",
        "email": "info@samsantech.kz",
    }

    recipients = [
        {
            "name": "Your Client",
            "email": email,
        }
    ]

    reply_to = [
        {
            "name": "SAMSANTECH",
            "email": "info@samsantech",
        }
    ]

    mailer.set_mail_from(mail_from, mail_body)
    mailer.set_mail_to(recipients, mail_body)
    mailer.set_subject(subject, mail_body)
    mailer.set_html_content("This is the HTML content", mail_body)
    mailer.set_plaintext_content("This is the text content", mail_body)
    mailer.set_reply_to(reply_to, mail_body)

    # using print() will also return status code and data
    time.sleep(5)
    mailer.send(mail_body)
    print("email send to", email)
    print(text)