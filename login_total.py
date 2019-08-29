import requests


# 登录url
url = ""

# 获取Cookie
def get_cookie(login_data):
    # 测试登录数据

    # login_data = read_data_csv()
    # print(login_data)

    lg_reqs = requests.post(url, data=login_data)
    cookie = lg_reqs.cookies
    print(cookie)
    return cookie

# get_cookie(login_data)

# 获取csv数据
def read_data_csv():
    # 打开文件
    with open('./data/login_data.csv', encoding='utf-8') as file:
        # 读取文件
        line_list = file.readlines()
    # 用户列表
    user_list = []
    # 遍历每行
    for line in line_list:
        # #注释掉不需要数据,
        if not line.startswith('#'):
            # strip去掉换行符,分割
            userName = line.strip().split(',')[0]
            userPass = line.strip().split(',')[1]
            # 定义字典
            dict = {'checkcode':'0000', 'remember':'Y'}
            #新增键值对
            dict['userName'] = userName
            dict['userPass'] = userPass
            #每条字典增添到列表中
            user_list.append(dict)
            # 直接调用login
            for i in user_list:
                get_cookie(i)
    # print(user_list)
    #print(dict)
    return user_list

# 获取数据
read_data_csv()
# li = read_data_csv()
# print(li)

# 获取登录数据
def get_login_data():
    user_list = read_data_csv()
    for i in user_list:
        login_data = i
    print(login_data)
    return login_data

# li = get_login_data()
# print(li)


# login_data = {'userName':'abc', 'userPass':'123', 'checkcode':'0000', 'remember':'Y'}



# if __name__ == '__main__':

# 整合传参
# get_cookie(li)

