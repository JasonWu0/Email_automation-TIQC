from email.message import EmailMessage
import ssl
import smtplib
import csv
import imghdr

image = ""
email_sender = #Email sender
email_reciever = #Email placeholder
email_password = #Email login
subject = input("What is the subject of this email?\n")
body = input("What is the body of this email?\n")
attached = input("Would you like to add an attachment?\n")
if attached.upper() == "YES" or attached.upper() == "Y":
    image = input("Image or PDF?\n")
    count = input("How many files?\n")
    file_list = []
    for x in range(int(count)):
        files = input("What is the file name?\n")
        if image.upper() == "IMAGE":
            file_list.append(files + ".jpeg")
        if image.upper() == "PDF":
            file_list.append(files + ".pdf")

def send_email():
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_reciever
    em["Subject"] = subject
    em.set_content(body)

    context =ssl.create_default_context()

    #TO add attachments
    if attached.upper() == "YES":
        if image.upper() == "IMAGE":
            for images in file_list:
                with open(images, "rb") as f:
                    file_data = f.read()
                    file_type = imghdr.what(f.name)
                    file_name = f.name
                em.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)
        if image.upper() == "PDF":
            for pdf in file_list:
                with open(pdf, "rb") as f:
                    file_data = f.read()
                    file_name = f.name
                em.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())


with open("emailslist.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        email_reciever = line[0]
        send_email()