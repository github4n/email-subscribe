import smtplib
import requests
import datetime
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import asyncio
from pyppeteer import launch
from common import *

content = """
<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Transitional//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'>
<html xmlns='http://www.w3.org/1999/xhtml'>
<head>
    <meta charset='utf-8'>
    <meta name='viewport' content='width=device-width'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title></title>
    <style type='text/css'>
        html,
        body {
            margin: 0 auto !important;
            padding: 0 !important;
            height: 100% !important;
            width: 100% !important;
        }
        * {
            -ms-text-size-adjust: 100%;
            -webkit-text-size-adjust: 100%;
        }
        div[style*='margin: 16px 0'] {
            margin:0 !important;
        }
        table,
        td {
            mso-table-lspace: 0pt !important;
            mso-table-rspace: 0pt !important;
        }
        table {
            border-spacing: 0 !important;
            border-collapse: collapse !important;
            table-layout: fixed !important;
            Margin: 0 auto !important;
        }
        table table table {
            table-layout: auto;
        }
        img {
            -ms-interpolation-mode:bicubic;
        }
        .mobile-link--footer a,
        a[x-apple-data-detectors] {
            color:inherit !important;
            text-decoration: underline !important;
        }
    </style>
    <style>
        .button-td,
        .button-a {
            transition: all 100ms ease-in;
        }
        .button-td:hover,
        .button-a:hover {
            background: #555555 !important;
            border-color: #555555 !important;
        }
        @media screen and (max-width: 480px) {
            .fluid,
            .fluid-centered {
                width: 100% !important;
                max-width: 100% !important;
                height: auto !important;
                Margin-left: auto !important;
                Margin-right: auto !important;
            }
            .fluid-centered {
                Margin-left: auto !important;
                Margin-right: auto !important;
            }
            .stack-column,
            .stack-column-center {
                display: block !important;
                width: 100% !important;
                max-width: 100% !important;
                direction: ltr !important;
            }
            .stack-column-center {
                text-align: center !important;
            }
            .center-on-narrow {
                text-align: center !important;
                display: block !important;
                Margin-left: auto !important;
                Margin-right: auto !important;
                float: none !important;
            }
            table.center-on-narrow {
                display: inline-block !important;
            }
        }
    </style>
</head>
<body width='100%' bgcolor='#222222' style='Margin: 0;'>
    <center style='width: 100%; background: #222222;'>
        <div style='max-width: 680px; margin: auto;'>
            <table cellspacing='0' cellpadding='0' border='0' align='center' width='100%' style='max-width: 680px;'>
                <tr>
                    <td style='padding: 20px 0; text-align: center'>
                    </td>
                </tr>
            </table>
            <table class='main' width='100%' cellpadding='0' cellspacing='0' style='font-family: STSong; box-sizing: border-box; font-size: 14px; border-radius: 3px; background-color: #fff; margin: 0; border: 1px solid #e9e9e9;' bgcolor='#fff'>
                <tr style='font-family: STSong; box-sizing: border-box; font-size: 14px; margin: 0;'><td class='alert alert-warning' style='font-family: STSong; box-sizing: border-box; font-size: 16px; vertical-align: top; color: #fff; font-weight: 500; text-align: center; border-radius: 3px 3px 0 0; background-color: #888888; margin: 0; padding: 20px;' align='center' bgcolor='#888888' valign='top'>
                            <b>嗨，亲爱的宝贝脑婆～</b>
                        </td>
                    </tr>
            </table>
            <table cellspacing='0' cellpadding='0' border='0' align='center' bgcolor='#ffffff' width='100%' style='max-width: 680px;'>
                <tr>
                    <td>
                        <img style="padding: 0.60em; background: white; box-shadow: 1px 1px 10px #999;" src="cid:xiaoxiaotimer" />
                    </td>
                </tr>
                <tr>
                    <td>
                        <table cellspacing='0' cellpadding='0' border='0' width='100%'>
                            <tr>
                                <td style='padding: 40px; text-align: left; font-family: sans-serif; font-size: 15px; mso-height-rule: exactly; line-height: 20px; color: #555555;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们都已经在一起这么多天啦！今天又是新的一天哦！<br>
                                    <br><br>
                                    <table cellspacing='0' cellpadding='0' border='0' align='center' style='Margin: auto'>
                                        <tr>
                                            <td style='border-radius: 3px; background: #222222; text-align: center;' class='button-td'>
                                                <a target='_blank' href='http://www.weather.com.cn/weather/101220801.shtml' style='background: #888888; border: 15px solid #888888; font-family: sans-serif; font-size: 13px; line-height: 1.1; text-align: center; text-decoration: none; display: block; border-radius: 3px; font-weight: bold;' class='button-a'>
                                                    &nbsp;&nbsp;&nbsp;&nbsp;<span style='color:#ffffff'>点击这里查看详细天气哦！</span>&nbsp;&nbsp;&nbsp;&nbsp;</a>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
            <table cellspacing='0' cellpadding='0' border='0' align='center' width='100%' style='max-width: 680px;'>
                <tr>
                    <td style='padding: 40px 10px;width: 100%;font-size: 12px; font-family: sans-serif; mso-height-rule: exactly; line-height:18px; text-align: center; color: #888888;'>
                      超级爱你的脑公～
                    </td>
                </tr>
            </table>
        </div>
    </center>
</body>
</html>
"""

IMAGE_NAME = "xiaoxiaotimer.png"

async def fetch():
    browser = await launch(
        {"args": ["--no-sandbox", "--disable-setuid-sandbox"]}
    )
    page = await browser.newPage()
    await page.goto("http://www.czxa.top/lovetimer/index.html")
    await page.screenshot(
        {
            "path": IMAGE_NAME,
            "clip": {"x": 0, "y": 90, "height": 340, "width": 750},
        }
    )
    await browser.close()


title = '图片发送测试'
mail_host = "smtp.sina.com"
mail_user = "czxjnu@sina.com"
mail_pass = "zssjmm126,"
sender = 'czxjnu@sina.com'
receivers = ['czxjnu@163.com']

def send_email():
    html_content = content
    msg = MIMEMultipart("alternative")
    msg['From'] = "{}".format(sender)
    msg['To'] = ",".join(receivers)
    msg['Subject'] = title

    with open(IMAGE_NAME, "rb") as f:
        img = MIMEImage(f.read())
        img.add_header("Content-ID", "one")
        msg.attach(img)
    msg.attach(MIMEText(html_content, "html", 'utf-8'))

    try:
        smtp_obj = smtplib.SMTP_SSL(mail_host, 465)
        smtp_obj.login(mail_user, mail_pass)
        smtp_obj.sendmail(sender, receivers, msg.as_string())
        smtp_obj.quit()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(fetch())
    except Exception:
        asyncio.get_event_loop().run_until_complete(fetch())
    send_email()
    import codecs
    f = codecs.open('xiaoxiaotimer.html', 'w', 'utf-8')
    f.write(content)
    f.close()
