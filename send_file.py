import paramiko
import time
import tkinter as tk
from tkinter import filedialog, font
import sys

def progress_bar(transferred, toBeTransferred, suffix=''):
    bar_len = 100
    filled_len = int(round(bar_len * transferred / float(toBeTransferred)))
    percents = round(100.0 * transferred / float(toBeTransferred), 1)
    bar = '\033[32;1m%s\033[0m' % '=' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('[%s] %s%s %s\r' % (bar, '\033[32;1m%s\033[0m' % percents, '%', suffix))
    sys.stdout.flush()

# def downfile():
#     """
#     下载文件
#     :param hostip:
#     :param parajson:
#     :return:
#     """
#     hostip=‘192.168.1.5’
#     sshport = '22'
#     password = 'sanshi@408'
#     oldfilepath = '/root/oracle-instantclient12.2-basic-12.2.0.1.0-1.x86_64.rpm'
#     newfilepath = '/root/oracle-instantclient12.2-basic-12.2.0.1.0-1.x86_64.rpm'

#     t = paramiko.Transport((hostip, int(sshport)))
#     t.connect(username='root', password=password)
#     sftp = paramiko.SFTPClient.from_transport(t)
#     sftp.get(oldfilepath, newfilepath, callback=progress_bar)
#     t.close()
#     return ''



remote_folder = '/home/sun/Desktop/'
local_folder = '/home/sun/Desktop/'

time_stamp = ''
for i in range(6):
	time_stamp += str(time.localtime(time.time())[i])

transport = paramiko.Transport(('192.168.1.101', 22))
transport.connect(username='sun', password='suns')
sftp = paramiko.SFTPClient.from_transport(transport)
#upload

root = tk.Tk()
root.geometry('400x400')
root.withdraw()


# print(font.families())

# filedialog.geometry('100x100')
file_path = filedialog.askopenfilename()
print(file_path.split('/')[-1])
sftp.put(file_path, remote_folder+time_stamp+'_'+file_path.split('/')[-1],callback=progress_bar,confirm=True)

#download
# file_name = input('remote Desktop file_name >')
# print(file_name)

# sftp.get(remote_folder+file_name, file_name)
# transport.close()