# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from picclass import Pic
import os
import filepathread
import shutil
import time
from datetime import datetime
import socket

fileName = []
fileNamePath = []

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(datetime.now())
    domain = "aip.baidubce.com"
    myaddr = socket.getaddrinfo(domain, 'https')
    print(str(domain) + " = " + myaddr[0][4][0])

    start = time.time()



    path = os.getcwd()
    #fileNamePath = filepathread.file_name(path)
    filepathread.listdir(path, fileNamePath)

    for file in fileNamePath:
        #path = r'D:\Program Files\Microsoft XNA\picpick 19.11.26\temporary 1st\1 (%d).jpg' % num
        if file.endswith('jpg') or file.endswith('JPG'):

            print(file)
            try:
                result = Pic(file)
            except:
                print('Class error')
                continue

            fileName = os.path.split(file) #分割路径【0】和文件【1】
            try:
                shutil.move(file, fileName[0] + '\\' + result + '\\' + fileName[1])
            except FileNotFoundError:
                os.mkdir(path + '\\' + result + '\\')
                print('已创建文件夹'+ result)
                shutil.move(file, fileName[0] + '\\' + result + '\\' + fileName[1])
            except PermissionError:     #文件占用
                print('文件占用')
                continue
            except FileExistsError:     #文件已存在
                print('文件已存在')
                continue
            except:
                print('文件移动错误')
                continue

        else:
            continue

    end = time.time()
    print('耗时时长: %1.2f s' % (end - start))
    os.system("pause")
    '''
    训练模型
    1 可选
    2 可能选
    3 可能不选
    4 不可选
    5 其他
    特征明显
    '''
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
