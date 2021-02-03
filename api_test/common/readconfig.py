import os
import configparser

cur_path = os.path.dirname(os.path.relpath(__file__))
configpath = os.path.join(cur_path,"email_config.ini")
conf_obj = configparser.ConfigParser()

conf_obj.read(configpath)
# class ReadEmailConfig():
#
#     def __init__(self,smtp_server,port,sender,receiver,subject):
#         self.smtp_server = smtp_server
#         self.port = port
#         self.sender = sender
#         self.receiver = receiver
#         self.subject = subject
def get_emailinfo(smtp_server,port,sender,pwd,receiver,subject):
    smtp_server = conf_obj.get('email',smtp_server)
    sender = conf_obj.get('email',sender)
    port = conf_obj.get('email',port)
    pwd = conf_obj.get('email',pwd)
    receiver = conf_obj.get('email',receiver)
    subject = conf_obj.get('email',subject)

    return [smtp_server,port,sender,pwd,receiver,subject]

if __name__ == '__main__':
    email_info = get_emailinfo("smtp_server","port","sender","pwd","receiver","subject")
    print(email_info)
    print(type(email_info))
    print(",".join(email_info))
    receiver_list = email_info[4:-1]
    print(receiver_list)
