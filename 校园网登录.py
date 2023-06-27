import os
import sys
import requests
import time

# 定义校园网登录 URL 的模板
LOGIN_URL_TEMPLATE = 'http://10.2.5.251:801/eportal/?c=Portal&a=login&login_method=1&user_account={account}%40{carrier}&user_password={password}'


# 从文件中读取账户信息的函数
def get_account_info(file_path):
    if not os.path.exists(file_path):
        # 如果文件不存在，则提示用户输入账户信息并保存到文件中
        account = input('请输入您的校园网账号（八位数字）：')
        carrier = input('请输入您的运营商（联通对应 unicom，电信对应 telecom，移动对应 mobile，请输入对应英文）：')
        password = input('请输入您的校园网密码：')
        with open(file_path, 'w') as f:
            f.write(f'{account}\n{carrier}\n{password}\n')
        print(r'如果需要开机自登录，请将校园网登录.exe或者它的快捷方式放入windows启动文件夹内，路径为 C:\Users\你的用户名\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')
        print(r'在运行中输入shell:startup,也可进入')
        print('这个界面会停留五秒')
        time.sleep(5)
    else:
        # 如果文件存在，则从文件中读取账户信息
        with open(file_path, 'r') as f:
            account, carrier, password = f.read().strip().split('\n')
    return account, carrier, password


# 将账户信息保存到文件的函数
def save_account_info(file_path, account, carrier, password):
    with open(file_path, 'w') as f:
        f.write(f'{account}\n{carrier}\n{password}\n')
    


# 发送登录请求并返回响应内容
def login(account, carrier, password):
    login_url = LOGIN_URL_TEMPLATE.format(account=account, carrier=carrier, password=password)
    response = requests.get(login_url)
    return response.text


if __name__ == '__main__':
    # 获取存储账户信息的文件路径
    home_dir = os.path.expanduser('~')
    login_dir = os.path.join(home_dir, 'Documents', 'login')
    os.makedirs(login_dir, exist_ok=True)
    account_info_file_path = os.path.join(login_dir, 'account_info.txt')
    
    # 读取或保存账户信息
    account, carrier, password = get_account_info(account_info_file_path)
    save_account_info(account_info_file_path, account, carrier, password)

    # 发送登录请求并解析响应内容
    response_text = login(account, carrier, password)
    print(response_text)
    if 'result":"1"' in response_text:
        print('登录成功')
        time.sleep(2)
    elif 'result":"0"' in response_text:
        print('您已登录，无需重复登录')
        time.sleep(2)
    else:
        print('登录失败，请检查是否已连接校园网')
        time.sleep(2)

    # 退出程序
    sys.exit()
