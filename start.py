# 在这个界面运行
# ctrl+c结束运行

import os
import time
from send import send_notice
from variable import path, frequency, notice


def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)


def get_FileModifyTime(filePath):
    # '''获取文件的修改时间'''
    t = os.path.getmtime(filePath)
    return TimeStampToTime(t)


def printHello():
    global newTime
    oldTime = newTime
    newTime = getTime()
    compareTime(oldTime, newTime)


def getTime():
    if __name__ == '__main__':
        return get_FileModifyTime(path)


def compareTime(oldTime, newTime):
    if __name__ == '__main__':
        if oldTime == newTime:
            print("没变")
        else:
            send_notice(notice+'\n时间戳： '+newTime)
            print("变了")


def loop_func(func, second):
    while True:
        func()
        time.sleep(second)


newTime = getTime()
loop_func(printHello, frequency)
