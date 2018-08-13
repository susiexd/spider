import urllib
# import urllib2
# import cookielib
from io import BytesIO
import lxml.html
from PIL import Image
import pytesseract


REGISTER_URL = 'http://example.webscraping.com/places/default/user/register'


def extract_image(html):
    ## 利用lxml获取表单中图像数据。图像数据的前缀定义了数据类型。
    tree = lxml.html.fromstring(html)
    img_data = tree.cssselect('div#recaptcha img')[0].get('src')
    ##利用逗号分割，将其分为两部分，移除该前缀。这是一张进行了base64编码的图像
    img_data = img_data.partition(',')[-1]
    #open('test_.png', 'wb').write(data.decode('base64'))
    ##进行base64解码，回到最初的二进制
    binary_img_data = img_data.decode('base64')
    ##要想加载该图片，PIL需要对一个类似文件的接口，在传给Image类，我们又使用ByteIO对这个二进制进行封装
    file_like = BytesIO(binary_img_data)
    img = Image.open(file_like)
    return img

def ocr(img):
    # threshold the image to ignore background and keep text
    #img.save('capcha_originl.png')
    gray = img.convert('L')
    #gray.save('captcha_greyscale.png')
    bw = gray.point(lambda x: 0 if x < 1 else 255, '1')##只保留阈值小于1的像素也就是全黑的像素才保留。
    #bw.save('captcha_threshold.png')
    #print bw
    word = pytesseract.image_to_string(bw)
    ascii_word = ''.join(c for c in word if c in string.letters).lower() ##将识别的每个字母连接起来组成验证码
    print(ascii_word)
    return ascii_word