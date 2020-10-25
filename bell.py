import time

from playsound import playsound

# 每次检测当前时间是否应该响铃的时间间隔
TIMEINTERVAL = 1

globals = {
    'true': True
}
with open("bellconf.json", "r", encoding="utf-8") as f:
    peojects = eval(f.read(), globals)


def getNowTime():
    '''
    获取当前已格式化的时间，格式：时:分
    :return: 返回格式化后的当前时间
    '''
    return time.strftime("%H:%M", time.localtime())


print(getNowTime())
print("程序开始运行，等待闹钟中")
while True:
    # 遍历项目
    for peoject in peojects:
        # 如果当前项目已经启用
        if peoject["enable"]:
            # 遍历项目中的闹钟
            for bell in peoject["bells"]:
                # 如果当前时间满足条件
                if getNowTime() == bell["time"]:
                    print("{} - {}".format(peoject["peojectname"], bell["name"]))
                    playsound(peoject["sound"])
    time.sleep(TIMEINTERVAL)
