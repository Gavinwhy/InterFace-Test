# 获取数据
def get_data():
    f=open("data.csv")

    li = f.readlines()

    for i in li:

        data_li = i.strip().split(",")

        print(data_li)
    return data_li

