# 构造请求正文
import requests



def test_add(add_data, expc_code, expc_reqs):        # 参数 - 数据驱动

    cookie = get_cookie()

    # 发送请求,添加cookies参数
    add_reqs = requests.post(url, data=add_data, cookies=cookie)

    print('###开始测试###')

    # 对响应码和响应正文断言
    actu_code = add_reqs.status_code
    actu_text = add_reqs.text

    if expc_code == actu_code and expc_reqs == actu_text:
        print('suc!')
    else:
        print('failed!')
        print('状态码:' + '预期 - ' + str(expc_code) + ', 实际 - ' + str(actu_code))
        print('响应:' + '预期 - ' + str(expc_reqs) + ', 实际 - ' + str(actu_text))

    print('###结束测试###')
