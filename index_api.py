import flask
from flask import render_template,request
import json
import requests

server = flask.Flask(__name__)

def getHeaders():
    return {"sourceType":"WEB"}

@server.route("/")
def index():

    return render_template("index.html")

@server.route("/index/",methods = ["GET","POST"])
def result():
    if request.method == "POST":
        if request.form.get("url"):
            # 从form表单中取到数据
            url = request.form.get("url")
            fun = request.form.get("fun")
            leixing = request.form.get("leixing")
            testdata = request.form.get("testdata")
            exr = request.form.get("exr")

            # 保存数据到字典中
            dict1 = {}
            dict1["url"] = url
            dict1["fun"] = fun
            dict1['leixing'] = leixing
            dict1["testdata"] = testdata
            dict1['exr'] = exr

            return render_template("index.html",data = exeData(dict1)[0],
                            data1 = exeData(dict1)[1] if exeData(dict1)[1] else  " ")
        else:
            data = {"message": "数据不能为空"}
            return render_template("index.html",urladr = data,data2 = data)


def exeData(dict1):
    """
    :param url: 接口地址
    :param fun: 请求类型
    :param leixing: 数据类型
    :param testdata: 请求参数
    :param exr: 预期结果
    :return:
    """
    # 获取字典中的url
    if dict1:
        url = dict1["url"]

        # 判断请求方法，根据方法名使用param或者data参数传入
        if dict1["fun"] == "post":
            param = dict1["testdata"]
            print(param)
            res = requests.post(url = url,data = param,headers = getHeaders())
            data1 = dict1["exr"]
            data = res.text
            return data,data1
        else:
            param = dict1["testdata"]
            if param:
                res = requests.get(url = url,params=param,headers = getHeaders())
                data = res.text
                data1 = dict1["exr"]
                print(res.url)
                return data,data1
            else:
                res = requests.get(url = url,headers = getHeaders())
                data = res.text
                data1 = dict1["exr"]
                return data,data1
                # response = requests.post(url = address_ip.registered(),data = json.dumps(data),headers= getHeaders())


def getResquest():
    url = "http://192.168.199.240:8061/sellerApi/sensitiveWord/replace"
    data = {"notice":"''''ssssss''''"}
    result = requests.post(url = url,data = json.dumps(data),headers = getHeaders())

    print(result.text)
    return result.text


if __name__ == '__main__':
    server.run(debug=True)
    exeData(result())
