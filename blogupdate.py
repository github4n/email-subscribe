import smtplib
import requests
import datetime
from email.header import Header
from email.mime.text import MIMEText

HEADERS = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}

def get_birth_days():
    """
    获取网站建立天数
    """
    today = datetime.datetime.today()
    anniversary = datetime.datetime(2017, 9, 29)
    return (today - anniversary).days

def get_today(today):
    """
    格式化今天日期
    """
    date = today["date"]
    week = today["data"]["forecast"][0]["date"][-3:]
    return "{}-{}-{}".format(date[:4], date[4:6], date[6:]), week

content = (
"今天是 {_date}，{_week}，自从2017年9月29日第一次建好个人网站以来，我的个人网站已经平稳的运行<strong style='font-family: STSong; box-sizing: border-box; font-size: 14px; margin: 0;'>{_loving_days}</strong>天啦！"
"</td>"
"</tr><tr style='font-family: STSong; box-sizing: border-box; font-size: 14px; margin: 0;'><td class='content-block' style='font-family: STSong; box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0; padding: 0 0 20px;' valign='top'>"
"<font color = '#FF9F00'><b>下面首先播报一下今日的天气：</b></font>"
"</td>"
"</tr>"
"<tr style='font-family: STSong; box-sizing: border-box; font-size: 14px; margin: 0;'>"
"<td class='content-block' style='font-family: STSong; box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0; padding: 0 0 20px;' valign='top'>"
"广州今日<font color='#E62739'><b>最{_g_weather_high}</font></b>，<b><font color='5E7CE2'>最{_g_weather_low}</font></b>，天气<b><font color='#381F21'>{_g_weather_type}</font></b>，"
"<br>需要注意{_g_weather_notice}呀!<br>"
"<tr style='font-family: STSong; box-sizing: border-box; font-size: 14px; margin: 0;'>"
"<td class='content-block' style='font-family: STSong; box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0; padding: 0 0 20px;' valign='top'>"
"<details>"
"<summary><strong>查看广州详细天气</strong></summary>"
"<b>广州今天</b>: <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#f37c3d'><b>日出时间为: {_g_sunrise}</b></font>;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><font color='#E62739'><b>最{_g_weather_high}</b></font>;</font><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><font color='5E7CE2'>最{_g_weather_low}</b></font>;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#aa3c16'><b>日落时间为: {_g_sunrset}</b></font>;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#f06966'><b>空气质量指数为: {_g_aqi}</b></font>;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#745285'><b>风向为: {_g_fx}</b></font>;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#854e4b'><b>风力大小为: {_g_fl}</b></font>;<br>天气<b><font color='#381F21'>{_g_weather_type}</font></b>，需要注意{_g_weather_notice}哦!<br><br>"
"<b>广州明天</b>: <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#f37c3d'><b>日出时间为: {_g_sunrise1}</b></font>;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><font color='#E62739'><b>最{_g_weather_high1}</b></font>;</font><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><font color='5E7CE2'>最{_g_weather_low1}</b></font>;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#aa3c16'><b>日落时间为: {_g_sunrset1}</b></font>;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#f06966'><b>空气质量指数为: {_g_aqi1}</b></font>;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#745285'><b>风向为: {_g_fx1}</b></font>;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#854e4b'><b>风力大小为: {_g_fl1}</b></font>;<br>天气<b><font color='#381F21'>{_g_weather_type1}</font></b>，需要注意{_g_weather_notice1}哦!<br><br>"
"<b>广州后天</b>: <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#f37c3d'><b>日出时间为: {_g_sunrise2}</b></font>;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><font color='#E62739'><b>最{_g_weather_high2}</b></font>;</font><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><font color='5E7CE2'>最{_g_weather_low2}</b></font>;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#aa3c16'><b>日落时间为: {_g_sunrset2}</b></font>;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#f06966'><b>空气质量指数为: {_g_aqi2}</b></font>;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#745285'><b>风向为: {_g_fx2}</b></font>;<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color='#854e4b'><b>风力大小为: {_g_fl2}</b></font>;<br>天气<b><font color='#381F21'>{_g_weather_type2}</font></b>，需要注意{_g_weather_notice2}哦!<br>"
"</details>"
"</td>"
"</tr>"
"<tr style='font-family: STSong; box-sizing: border-box; font-size: 14px; margin: 0;'><td class='content-block' style='font-family: STSong; box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0; padding: 0 0 20px;' valign='top'>"
)

def get_weather_info():
    """
    获取天气信息
    """
    weather_api = "https://www.sojson.com/open/api/weather/json.shtml?city={}"
    girl = requests.get(weather_api.format("广州", headers = HEADERS)).json()
    girl_weather = girl['data']['forecast'][0]
    girl_weather1 = girl['data']['forecast'][1]
    girl_weather2 = girl['data']['forecast'][2]
    _date, _week = get_today(girl)
    if girl:
        return content.format(
            _week=_week,
            _date=_date,
            _loving_days=get_birth_days(),
            _g_weather_high=girl_weather["high"],
            _g_weather_low=girl_weather["low"],
            _g_weather_type=girl_weather["type"],
            _g_weather_notice=girl_weather["notice"],
            _g_aqi=girl_weather["aqi"],
            _g_sunrise=girl_weather["sunrise"],
            _g_sunrset=girl_weather["sunset"],
            _g_fl=girl_weather["fl"],
            _g_fx=girl_weather["fx"],
            _g_weather_high1=girl_weather1["high"],
            _g_weather_low1=girl_weather1["low"],
            _g_weather_type1=girl_weather1["type"],
            _g_weather_notice1=girl_weather1["notice"],
            _g_aqi1=girl_weather1["aqi"],
            _g_sunrise1=girl_weather1["sunrise"],
            _g_sunrset1=girl_weather1["sunset"],
            _g_fl1=girl_weather1["fl"],
            _g_fx1=girl_weather1["fx"],
            _g_weather_high2=girl_weather2["high"],
            _g_weather_low2=girl_weather2["low"],
            _g_weather_type2=girl_weather2["type"],
            _g_weather_notice2=girl_weather2["notice"],
            _g_aqi2=girl_weather2["aqi"],
            _g_sunrise2=girl_weather2["sunrise"],
            _g_sunrset2=girl_weather2["sunset"],
            _g_fl2=girl_weather2["fl"],
            _g_fx2=girl_weather2["fx"],
        )

def new_post():
	url = "http://www.czxa.top/content.json"
	json = requests.get(url.format(headers = HEADERS)).json()['posts']
	post = (get_weather_info(), 
        "<font color = '#FF9F00'><b>然后我要播报一下最近网站的更新信息，",
        "最近网站更新的文章有：</b></font>", 
        "</td></tr><tr style='font-family: STSong; box-sizing: border-box; font-size: 14px; margin: 0;'>",
        "<td class='content-block' style='font-family: STSong; box-sizing: border-box;", 
        "font-size: 14px; vertical-align: top; margin: 0; padding: 0 0 20px;' valign='top'>")
	for i in range(0, 8):
		post = post + ("<font color = '#348eda'><b>", json[i]['date'][0:10], ": ", "</b></font><a href='", json[i]['permalink'], "'>", json[i]['title'], "</a><br>")
	post = post + (
		"<font color = '#FF9F00'><b>此外，", 
		"最近笔记本更新的文章有：</b></font>", 
		"</td></tr><tr style='font-family: STSong; box-sizing: border-box; font-size: 14px; margin: 0;'>",
        "<td class='content-block' style='font-family: STSong; box-sizing: border-box;", 
        "font-size: 14px; vertical-align: top; margin: 0; padding: 0 0 20px;' valign='top'>")
	url2 = "http://www.czxa.top/notes/content.json"
	json2 = requests.get(url2.format(headers = HEADERS)).json()['posts']
	for i in range(0, 8):
		post = post + ("<font color = '#348eda'><b>", json2[i]['date'][0:10], ": ", "</b></font><a href='http://www.czxa.top/notes/", json2[i]['path'], "'>", json2[i]['title'], "</a><br>")
	return ''.join(post)


subscribe = (
"<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Transitional//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'><html xmlns='http://www.w3.org/1999/xhtml' style='font-family: STSong; box-sizing: border-box; font-size: 14px; margin: 0;'>", 
"<head>", 
"<meta name='viewport' content='width=device-width' />", 
"<meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />", 
"<title>订阅邮件</title>", 
"<style type='text/css'>", 
"img {", 
"max-width: 100%;", 
"}", 
"body {", 
"-webkit-font-smoothing: antialiased; -webkit-text-size-adjust: none; width: 100% !important; height: 100%; line-height: 1.6em;", 
"}", 
"body {", 
"background-color: #f6f6f6;", 
"}", 
"a:link,a:visited{",
" text-decoration:none;",
"}",
"a:hover{",
" text-decoration:underline;",
"}",
"@media only screen and (max-width: 640px) {", 
"body {", 
"  padding: 0 !important;", 
"}", 
"h1 {", 
"  font-weight: 800 !important; margin: 20px 0 5px !important;", 
"}", 
"h2 {", 
"  font-weight: 800 !important; margin: 20px 0 5px !important;", 
"}", 
"h3 {", 
"  font-weight: 800 !important; margin: 20px 0 5px !important;", 
"}", 
"h4 {", 
"  font-weight: 800 !important; margin: 20px 0 5px !important;", 
"}", 
"h1 {", 
"  font-size: 22px !important;", 
"}", 
"h2 {", 
"  font-size: 18px !important;", 
"}", 
"h3 {", 
"  font-size: 16px !important;", 
"}", 
".container {", 
"  padding: 0 !important; width: 100% !important;", 
"}", 
".content {", 
"  padding: 0 !important;", 
"}", 
".content-wrap {", 
"  padding: 10px !important;", 
"}", 
".invoice {", 
"  width: 100% !important;", 
"}", 
"}", 
"</style>", 
"</head>", 
"<body itemscope itemtype='http://schema.org/EmailMessage' style='font-family: STSong; box-sizing: border-box; font-size: 14px; -webkit-font-smoothing: antialiased; -webkit-text-size-adjust: none; width: 100% !important; height: 100%; line-height: 1.6em; background-color: #f6f6f6; margin: 0;' bgcolor='#f6f6f6'>", 
"<table class='body-wrap' style='font-family: STSong; box-sizing: border-box; font-size: 14px; width: 100%; background-color: #f6f6f6; margin: 0;' bgcolor='#f6f6f6'><tr style='font-family: STSong; box-sizing: border-box; font-size: 14px; margin: 0;'><td style='font-family: STSong; box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0;' valign='top'></td>", 
"<td class='container' width='600' style='font-family: STSong; box-sizing: border-box; font-size: 14px; vertical-align: top; display: block !important;max-width: 600px !important; clear: both !important; margin: 0 auto;' valign='top'>", 
"<div class='content' style='font-family: STSong; box-sizing: border-box; font-size: 14px; max-width: 600px; display: block; margin: 0 auto; padding: 20px;'>", 
"                <table class='main' width='100%' cellpadding='0' cellspacing='0' style='font-family: STSong; box-sizing: border-box; font-size: 14px; border-radius: 3px; background-color: #fff; margin: 0; border: 1px solid #e9e9e9;' bgcolor='#fff'><tr style='font-family: STSong; box-sizing: border-box; font-size: 14px; margin: 0;'><td class='alert alert-warning' style='font-family: STSong; box-sizing: border-box; font-size: 16px; vertical-align: top; color: #fff; font-weight: 500; text-align: center; border-radius: 3px 3px 0 0; background-color: #FF9F00; margin: 0; padding: 20px;' align='center' bgcolor='#FF9F00' valign='top'>", 
"<b>你好，欢迎订阅我的博客～</b>", 
"</td>", 
"</tr><tr style='font-family: STSong; box-sizing: border-box; font-size: 14px; margin: 0;'><td class='content-wrap' style='font-family: STSong; box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0; padding: 20px;' valign='top'>", 
"<table width='100%' cellpadding='0' cellspacing='0' style='font-family: STSong; box-sizing: border-box; font-size: 14px; margin: 0;'><tr style='font-family: STSong; box-sizing: border-box; font-size: 14px; margin: 0;'>", 
"<td class='content-block' style='font-family: STSong; box-sizing: border-box; font-size: 14px; vertical-align: top; margin: 0; padding: 0 0 20px;' valign='top'>")
def news():
    url = "http://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=1"
    json = requests.get(url.format(headers = HEADERS)).json()['result']['data']
    news = (new_post(), 
        "</td></tr><tr style='font-family: STSong; box-sizing: border-box; font-size: 14px; margin: 0;'>",
        "<td class='content-block' style='font-family: STSong; box-sizing: border-box; font-size: 14px;",
        " vertical-align: top; margin: 0; padding: 0 0 20px;' valign='top'>",
        "<font color = '#FF9F00'><b>最后，要保持对新闻的关注！再插播一些即时新闻：",
        "</b></font></td></tr><tr style='font-family: STSong;", 
        "box-sizing: border-box; font-size: 14px; margin: 0;'>",
        "<td class='content-block' style='font-family: STSong;", 
        "box-sizing: border-box; font-size: 14px; vertical-align: top;",
        "margin: 0; padding: 0 0 20px;' valign='top'>")
    for i in range(0, 50):
        j = i + 1
        if j == 6:
            news = news + ("<details>", "<summary><strong>查看更多</strong></summary>")
        news = news + ("<font color = '#348eda'><b>", str(j), ": </b></font><a href=", json[i]['url'], ">", json[i]['title'], "</a><br>")
    news = subscribe + news + ("</details>", "</td></tr><tr style='font-family: STSong; box-sizing: border-box;",
        "font-size: 14px; margin: 0;'><td class='content-block' style='font-family:",
        "STSong; box-sizing: border-box; font-size: 14px; vertical-align: top;",
        "margin: 0; padding: 0 0 20px;' valign='top'><center><a href='http://www.czxa.top'",
        "target='_blank' class='btn-primary' style='font-family: STSong; box-sizing: border-box;",
        "font-size: 14px; color: #FFF; text-decoration: none; line-height: 2em; font-weight: bold;",
        "text-align: center; cursor: pointer; display: inline-block; border-radius: 5px;",
        "text-transform: capitalize; background-color: #348eda; margin: 0; border-color: #348eda;",
        "border-style: solid; border-width: 10px 20px;'>访问我的个人博客</a></center></td></tr><tr ",
        "style='font-family: STSong; box-sizing: border-box; font-size: 14px; margin: 0;'><td ",
        "class='content-block' style='font-family: STSong; box-sizing: border-box; font-size: 14px;", 
        "vertical-align: top; margin: 0; padding: 0 0 20px;' valign='top'>谢谢你的关注！</td></tr></table></td>",
        "</tr></table><div class='footer' style='font-family: STSong; box-sizing: border-box; ",
        "font-size: 14px; width: 100%; clear: both; color: #999; margin: 0; padding: 20px;'>",
        "<table width='100%' style='font-family: STSong; box-sizing: border-box; font-size:",
        "14px; margin: 0;'><tr style='font-family: STSong; box-sizing: border-box; font-size:",
        "14px; margin: 0;'>",
        "<tr style='font-family: STSong; box-sizing: ",
        "border-box; font-size: 14px; margin: 0;'>",
        "<td class='aligncenter content-block' style='font-family: ",
        "STSong; font-size: 12px; vertical-align: top; color: #999; ",
        "text-align: center; margin: 0; padding: 0 0 20px;'",
        "align='center' valign='top'><a href='http://www.czxa.top' style='font-family: STSong; box-sizing: border-box; font-size: 12px; color: #999; text-decoration: underline; margin: 0;'>©️ 2018 程振兴</a></td>",
        "</tr></table></div></div></td>",
        "<td style='font-family: STSong;",
        "box-sizing: border-box; font-size: 14px; vertical-align: top;",
        "margin: 0;' valign='top'></td></tr></table></body></html>")
    return ''.join(news)

title = 'czxa.top更新提醒'
mail_host = "smtp.sina.com"
mail_user = "czxjnu@sina.com"
mail_pass = "zssjmm126,"
sender = 'czxjnu@sina.com'
receivers = ['czxjnu@163.com', '2591001813@qq.com', '438970103@qq.com', '18810860259@yeah.net', '362540567@qq.com', '1143453386@qq.com', '411509829@qq.com']
# receivers = ['czxjnu@163.com']

def sendEmail():
    message = MIMEText(news(), 'html', 'utf-8')
    # print(message)
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
    # sendEmail()
    import codecs
    f = codecs.open('email.html', 'w', 'utf-8')
    f.write(news())
    f.close()
