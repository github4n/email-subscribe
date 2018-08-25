import smtplib
import requests
import datetime
from email.header import Header
from email.mime.text import MIMEText

def get_birth_days():
    """
    获取丁文亮的出生天数
    """
    today = datetime.datetime.today()
    anniversary = datetime.datetime(1998, 1, 6)
    return (today - anniversary).days

def get_today(today):
    """
    格式化今天日期
    """
    date = today["date"]
    week = today["data"]["forecast"][0]["date"][-3:]
    return "{}-{}-{}".format(date[:4], date[4:6], date[6:]), week

content = (
    "丁文亮同学，下面我郑重地通知你:<br>"
    "今天是 {_date}，{_week}，是你生命中的第<font color='#9068be'>{_loving_days}</font>天。<br>"
    "你那里明天<font color='#E62739'>最{_g_weather_high}</font>，<font color='5E7CE2'>最{_g_weather_low}</font>，天气<font color='#381F21'>{_g_weather_type}</font>，<br>"
    "需要注意{_g_weather_notice}。"
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
    girl = requests.get(weather_api.format("广州", headers = HEADERS)).json()
    girl_weather = girl['data']['forecast'][1]
    _date, _week = get_today(girl)
    if girl:
        return content.format(
            _week=_week,
            _date=_date,
            _loving_days=get_birth_days(),
            _g_weather_high=girl_weather["high"],
            _g_weather_low=girl_weather["low"],
            _g_weather_type=girl_weather["type"],
            _g_weather_notice=girl_weather["notice"]
        )

title = '程振兴的日常问候～'
mail_host = "smtp.126.com"
mail_user = "czxjnu@126.com"
mail_pass = "zssjmm126"
sender = 'czxjnu@126.com'
receivers = ['2591001813@qq.com', 'czxjnu@163.com']

def sendEmail():
    message = MIMEText(get_weather_info(), 'html', 'utf-8')
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
