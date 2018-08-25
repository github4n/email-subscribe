import smtplib
import requests
import datetime
from email.header import Header
from email.mime.text import MIMEText


def get_loving_days():
    """
    获取恋爱天数
    """
    today = datetime.datetime.today()
    anniversary = datetime.datetime(2017, 1, 6)
    return (today - anniversary).days

def get_today(today):
    """
    格式化今天日期
    """
    date = today["date"]
    week = today["data"]["forecast"][0]["date"][-3:]
    return "{}-{}-{}".format(date[:4], date[4:6], date[6:]), week

content = (
    "宝贝脑婆～:\n\n\t"
    "今天是 {_date}，{_week}。\n\t"
    "首先，今天已经是我们相恋的第 {_loving_days} 天了喔。下面我要播送天气预报啦！！\n\n\t"
    "你那里明天最{_g_weather_high}，最{_g_weather_low}，天气 {_g_weather_type}，"
    "注意{_g_weather_notice}\n\n\t哦！"
) # 邮件内容

def get_weather_info():
    """
    获取天气信息
    """
    weather_api = "https://www.sojson.com/open/api/weather/json.shtml?city={}"
    HEADERS = {
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
        "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    }
    girl = requests.get(weather_api.format("阜阳", headers = HEADERS)).json()
    girl_weather = girl['data']['forecast'][1]
    _date, _week = get_today(girl)
    if girl:
        return content.format(
            _week=_week,
            _date=_date,
            _loving_days=get_loving_days(),
            _g_weather_high=girl_weather["high"],
            _g_weather_low=girl_weather["low"],
            _g_weather_type=girl_weather["type"],
            _g_weather_notice=girl_weather["notice"]
        )


title = '脑公的日常问候～'
mail_host = "smtp.126.com"
mail_user = "czxjnu@126.com"
mail_pass = "zssjmm126"
sender = 'czxjnu@126.com'
receivers = ['czxjnu@163.com']

def sendEmail():
    message = MIMEText(get_weather_info(), 'plain', 'utf-8')
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功！")
    except smtplib.SMTPException as e:
        print(e)

if __name__ == '__main__':
    sendEmail()
