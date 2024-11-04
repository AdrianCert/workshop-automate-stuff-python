import win32com.client as win32

# outlook_obj = win32.Dispatch("outlook.application")
# mail_obj = outlook_obj.CreateItem(0)
# mail_obj.Subject = "La multi ani"
# mail_obj.To = "myname.blabla@gmail.com"
# mail_obj.Body = "La multi ani from python!!"
# mail_obj.Send()


def send_main(subject, to, body):
    outlook_obj = win32.Dispatch("outlook.application")

    mail_obj = outlook_obj.CreateItem(0)
    mail_obj.Subject = subject
    mail_obj.To = to
    mail_obj.HTMLBody = body

    mail_obj.Send()
